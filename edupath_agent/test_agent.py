import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_agent(message: str, user_id: str = "student_001", session_id: str = "session_001"):
    """Test the EduPath agent with a message."""
    print(f"\n{'='*60}")
    print(f"📤 Sending: {message}")
    print(f"{'='*60}\n")
    
    try:
        response = requests.post(
            f"{BASE_URL}/run",
            params={
                "user_input": message,
                "user_id": user_id,
                "session_id": session_id
            }
        )
        
        result = response.json()
        
        if result["status"] == "success":
            print(f"✅ SUCCESS\n")
            print(f"📥 Response:\n{result['response']}\n")
        else:
            print(f"❌ ERROR\n")
            print(f"Error: {result['response']}\n")
            if "traceback" in result:
                print(f"Traceback:\n{result['traceback']}\n")
                
        return result
        
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return None

if __name__ == "__main__":
    # Test 1: Math tutoring
    test_agent(
        "I got a math problem wrong: What is 15 + 27? I answered 41.",
        user_id="john_doe",
        session_id="math_session_1"
    )
    
    # Test 2: Scholarship search
    test_agent(
        "Find me scholarships for physics students",
        user_id="jane_smith",
        session_id="scholarship_session_1"
    )
    
    # Test 3: Parent liaison
    test_agent(
        "Show me my child's progress history",
        user_id="parent_001",
        session_id="parent_session_1"
    )