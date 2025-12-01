import time
import logging
from typing import Dict, Any
from src.core.memory import db

logger = logging.getLogger("EduPath.Tools")

# --- CUSTOM TOOL FUNCTIONS ---

def mcp_weakness_logger_func(student: str, topic: str, severity: str) -> Dict[str, Any]:
    """
    Logs a student's weakness to the database.
    """
    db.log_weakness(student, topic, severity)
    logger.info(f"📝 Logged weakness: {student} -> {topic} ({severity})")
    return {"status": "success", "message": f"Logged {topic} for {student}"}

def check_class_alerts_func() -> str:
    """Checks the database for class-wide failure trends."""
    result = db.check_class_trends()
    logger.info(f"📊 Analytics check: {result[:50]}...")
    return result

def get_student_history_func(student_name: str) -> str:
    """Retrieves a specific student's record."""
    history = db.get_student_history(student_name)
    logger.info(f"📚 Retrieved history for {student_name}")
    return history

def request_approval_func(plan: str, tool_context=None) -> str:
    """
    Simulates a Human-in-the-Loop pause.
    Returns approval and signals the loop to exit.
    """
    logger.info("⏸️ [PAUSE] Waiting for Teacher Approval...")
    logger.info(f"Plan submitted: {plan[:100]}...")
    time.sleep(1) 
    logger.info("▶️ [RESUME] Teacher Approved.")
    
    # Signal the loop to exit by setting escalate=True
    if tool_context and hasattr(tool_context, 'actions'):
        tool_context.actions.escalate = True
        logger.info("✅ Loop will exit after this iteration")
    
    return "APPROVED_BY_HUMAN"

# --- EXPORT FUNCTIONS DIRECTLY AS TOOLS ---
weakness_tool = mcp_weakness_logger_func
analytics_tool = check_class_alerts_func
history_tool = get_student_history_func
approval_tool = request_approval_func