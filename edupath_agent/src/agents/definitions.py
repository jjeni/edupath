from google.adk.agents import LlmAgent

# --- OFFICIAL ADK TOOLS ---
try:
    from google.adk.tools.google_search import GoogleSearchTool
    google_search_tool = GoogleSearchTool()
except:
    # Fallback mock
    def google_search_tool(q): 
        return "Mock: Physics scholarships"

try:
    from google.adk.tools.code_execution import CodeExecutionTool
    code_execution_tool = CodeExecutionTool()
except:
    # Fallback mock
    def code_execution_tool(code): 
        return "Mock code output"


# CUSTOM TOOLS
from src.tools.registry import weakness_tool, analytics_tool, history_tool, approval_tool


# --- 1) SCOUT AGENT ---
scout_agent = LlmAgent(
    name="Scout",
    model="gemini-1.5-flash",
    instruction="You are a Scholarship Scout. Use google_search to find live opportunities.",
    tools=[google_search_tool]
)

# --- 2) TUTOR AGENT ---
tutor_agent = LlmAgent(
    name="Tutor",
    model="gemini-1.5-flash",
    instruction="""
    You are an expert Math Tutor.
    Use code_execution to check answers.
    If wrong, explain and log via log_student_weakness.
    """,
    tools=[code_execution_tool, weakness_tool]
)

# --- 3) PLANNER AGENT ---
planner_agent = LlmAgent(
    name="Planner",
    model="gemini-1.5-flash",
    instruction="Create a remedial plan and then call request_approval to finalize.",
    tools=[approval_tool]
)

# --- 4) CRITIC AGENT ---
critic_agent = LlmAgent(
    name="Critic",
    model="gemini-1.5-flash",
    instruction="Review the plan. If request_approval was not used, reject the plan."
)

# --- 5) LIAISON AGENT ---
liaison_agent = LlmAgent(
    name="Liaison",
    model="gemini-1.5-pro",
    instruction="""
    Summarize findings for parents.
    Run check_class_alerts to check performance alerts.
    Use get_student_history if parent asks for history.
    """,
    tools=[analytics_tool, history_tool]
)