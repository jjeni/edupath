import os
import uvicorn
from fastapi import FastAPI
from google.genai import types
import time
import asyncio

# Import ADK components
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService, Session

# Import our workflow
from src.workflow import create_edupath_workflow

# Ensure API Key is set
if not os.environ.get("GOOGLE_API_KEY"):
    print("\n⚠️  WARNING: GOOGLE_API_KEY is not set. The agent will crash if you try to run it.")
    print("👉 Set it via: $env:GOOGLE_API_KEY='your_key' (PowerShell) or set GOOGLE_API_KEY=your_key (CMD)\n")

# 1. Initialize Workflow
workflow = create_edupath_workflow()

# 2. Initialize Session Service and Runner
APP_NAME = "EduPathApp"
session_service = InMemorySessionService()
runner = Runner(
    agent=workflow,
    app_name=APP_NAME,
    session_service=session_service
)

# 3. Create FastAPI Server
app = FastAPI(title="EduPath Enterprise Agent")

@app.get("/")
async def root():
    """Root endpoint with status information."""
    return {
        "service": "EduPath Enterprise Agent",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "run": "/run (POST)",
            "docs": "/docs",
            "health": "/health"
        },
        "api_key_set": bool(os.environ.get("GOOGLE_API_KEY"))
    }

@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "api_key_set": bool(os.environ.get("GOOGLE_API_KEY"))
    }

async def ensure_session_exists(user_id: str, session_id: str):
    """Ensure a session exists using the proper async API."""
    try:
        # Try to get the session using the async method
        session = await session_service.get_session(
            app_name=APP_NAME,
            user_id=user_id,
            session_id=session_id
        )
        print(f"✓ Session exists: {session_id}")
        return session
    except Exception as e:
        # Session doesn't exist, create it
        print(f"⚠️  Session not found: {e}")
        print(f"✨ Creating new session: {session_id} for user: {user_id}")
        
        # Create session object
        new_session = Session(
            id=session_id,
            app_name=APP_NAME,
            user_id=user_id,
            state={},
            events=[],
            last_update_time=time.time()
        )
        
        # Store using the async method - we need to await update_session
        await session_service.update_session(new_session)
        
        print(f"✅ Session created: {session_id}")
        return new_session

@app.post("/run")
async def run_workflow(user_input: str, user_id: str = "student_001", session_id: str = "session_001"):
    """
    Endpoint to trigger the full multi-agent workflow.
    
    Parameters:
    - user_input: The input message/query
    - user_id: User identifier (default: student_001)
    - session_id: Session identifier (default: session_001)
    """
    print(f"\n{'='*60}")
    print(f"📨 Input: {user_input[:50]}...")
    print(f"👤 User: {user_id}, Session: {session_id}")
    print(f"{'='*60}\n")
    
    # Check API key
    if not os.environ.get("GOOGLE_API_KEY"):
        return {
            "response": "ERROR: GOOGLE_API_KEY not set. Please set your API key and restart the server.",
            "status": "error"
        }
    
    try:
        # Ensure session exists
        await ensure_session_exists(user_id, session_id)
        
        # Create content
        content = types.Content(
            role='user',
            parts=[types.Part(text=user_input)]
        )
        
        # Run the agent asynchronously
        final_response = ""
        event_count = 0
        
        print(f"🚀 Starting agent execution...\n")
        
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=content
        ):
            event_count += 1
            print(f"📊 Event {event_count}: author={event.author}")
            
            # Collect the final response
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        final_response += part.text
                        print(f"   💬 {part.text[:100]}...")
        
        print(f"\n✅ Completed. Events processed: {event_count}\n")
        
        return {
            "response": final_response if final_response else "No response generated",
            "user_id": user_id,
            "session_id": session_id,
            "events_processed": event_count,
            "status": "success"
        }
        
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        print(f"\n❌ Error occurred:\n{error_trace}\n")
        return {
            "response": f"Runtime Error: {str(e)}",
            "traceback": error_trace,
            "status": "error"
        }

if __name__ == "__main__":
    print("--- 🚀 EDUPATH AGENT LISTENING ---")
    print(f"API Key Set: {bool(os.environ.get('GOOGLE_API_KEY'))}")
    print("Docs: http://127.0.0.1:8000/docs")
    print("Root: http://127.0.0.1:8000/")
    print(f"App Name: {APP_NAME}")
    uvicorn.run(app, host="127.0.0.1", port=8000)