🎓 EduPath Navigator EnterpriseAI-Powered Educational OrchestratorBuilt with Google Agent Development Kit (ADK), Gemini 1.5, and FastAPI.🏆 Project OverviewEduPath Navigator Enterprise is an autonomous multi-agent system designed to solve the "Time & Discovery" crisis in education. By leveraging a sophisticated Parallel-Loop-Sequential workflow, it acts as an always-on teaching assistant and guidance counselor.The system automates the educational support lifecycle:Discovery: Scanning for scholarships and opportunities in real-time.Assessment: Grading homework with code execution and identifying knowledge gaps.Planning: Iteratively designing remedial study plans with human oversight.Communication: synthesizing daily reports for parents and triggering class-wide alerts for teachers.🧠 ArchitectureThe system uses the Google Agent Development Kit (ADK) to orchestrate five specialized agent personas into a cohesive graph.%%{init: {'theme': 'dark', 'themeVariables': { 'fontSize': '16px', 'fontFamily': 'arial', 'primaryColor': '#2d4059', 'edgeLabelBackground':'#222'}}}%%
graph LR
    %% -- MAIN ORCHESTRATOR --
    Root(🤖 EduPath_Root<br/><i>Sequential Agent</i>):::root_style

    %% -- PHASE 1: PARALLEL GROUP --
    subgraph Parallel_Phase ["<b>Research & Grading Phase</b> <br/> <i>(Parallel Execution)</i>"]
        direction TB
        
        Scout(🕵️ Scout Agent):::agent_style
        Scout --> T_Search(🔧 google_search):::tool_style
        
        Tutor(👩‍🏫 Tutor Agent):::agent_style
        Tutor --> T_Code(🔧 code_execution):::tool_style
        Tutor --> T_Weakness(🔧 log_student_weakness):::tool_style
    end

    %% -- PHASE 2: LOOP GROUP --
    subgraph Loop_Phase ["<b>Planning Loop</b> <br/> <i>(Iterative Refinement)</i>"]
        direction TB
        
        Planner(📅 Planner Agent):::agent_style
        Critic(⚖️ Critic Agent):::agent_style
        
        Planner <-->|Draft & Review| Critic
        Critic --> T_Approve(🔧 request_teacher_approval):::tool_style
    end

    %% -- PHASE 3: FINALIZER --
    Liaison(📢 Liaison Agent):::agent_style
    Liaison --> T_Analytics(🔧 check_class_alerts):::tool_style
    Liaison --> T_History(🔧 get_student_history):::tool_style

    %% -- CONNECTIONS --
    Root ==> Parallel_Phase
    Root ==> Loop_Phase
    Root ==> Liaison

    %% -- STYLING --
    classDef root_style fill:#1b5e20,stroke:#66bb6a,stroke-width:2px,color:white;
    classDef agent_style fill:#37474f,stroke:#90a4ae,stroke-width:2px,color:white;
    classDef tool_style fill:#263238,stroke:#78909c,stroke-width:1px,color:#b0bec5,stroke-dasharray: 5 5;
    
    style Parallel_Phase fill:#00000000,stroke:#eceff1,stroke-width:2px,color:#eceff1
    style Loop_Phase fill:#00000000,stroke:#eceff1,stroke-width:2px,color:#eceff1
🤖 The Agent TeamAgentRoleModelKey ToolsScoutResearcherGemini 1.5 FlashGoogle SearchTutorAcademic GraderGemini 1.5 Flashcode_execution, log_student_weaknessPlannerStrategistGemini 1.5 FlashN/ACriticQuality ControlGemini 1.5 Flashrequest_teacher_approval (Human-in-the-Loop)LiaisonCommunicatorGemini 1.5 Procheck_class_alerts, get_student_history✨ Key Features⚡ Parallel Execution: The Scout and Tutor run simultaneously to minimize latency.🔄 Iterative Planning Loop: The Planner and Critic engage in a feedback loop until a study plan is approved by a human teacher.💾 Long-Term Memory (Memory Bank): A persistent SQLite database stores student histories and weakness logs, allowing the agent to recall context across different sessions.🛠️ Custom Tools (MCP): Implements the Model Context Protocol for structured logging (log_student_weakness) and system analytics (check_class_trends).📉 Context Compaction: Automatically summarizes conversation history to manage token limits effectively.🚀 Installation & SetupPrerequisitesPython 3.10 or higherA Google Cloud Project (for Vertex AI) or a Google AI Studio API Key.1. Clone the Repositorygit clone [https://github.com/YOUR_USERNAME/edupath-navigator.git](https://github.com/YOUR_USERNAME/edupath-navigator.git)
cd edupath-navigator
2. Set Up Virtual Environmentpython -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. Install Dependenciespip install -r requirements.txt
4. Configure API KeyCreate a .env file or set the environment variable directly:Windows (Command Prompt):set GOOGLE_API_KEY=your_actual_api_key_here
Mac/Linux (Terminal):export GOOGLE_API_KEY=your_actual_api_key_here
🏃‍♂️ UsageThis project uses FastAPI to serve the agent as a REST API.Start the Serverpython main.py
The server will start at http://127.0.0.1:8000Interact via Swagger UIOpen your browser to https://www.google.com/search?q=http://127.0.0.1:8000/docsClick POST /run -> Try it out.Enter a sample query based on the persona you want to test:🎓 Student Persona"My name is Alex. I am in Grade 11 and interested in Physics. Here is my Calculus Homework: Question: What is the integral of 2x? Answer: x^2 + C. Question: What is the derivative of x^3? Answer: 5x (I think this might be wrong)."👪 Parent Persona"I am Alex's parent. Can you please generate a report card of his recent performance and any specific weaknesses he has shown?"👨‍🏫 Teacher Persona"SYSTEM ADMIN CHECK: Please run the class-wide analytics tool. Are there any topics that require a class reschedule?"📂 Project Structureedupath-navigator/
├── src/
│   ├── agents/                 # Agent Definitions (Scout, Tutor, Liaison)
│   ├── core/                   # Database & Config (SQLite Memory Bank)
│   ├── tools/                  # Tool Logic (MCP Loggers, Analytics)
│   └── workflow.py             # Orchestration Graph (Parallel/Loop/Seq)
├── main.py                     # FastAPI Entry Point
├── requirements.txt            # Python Dependencies
└── edupath_enterprise.db       # Local Database (Auto-generated)
📄 LicenseThis project is licensed under the Apache 2.0 License - see the LICENSE file for details.Submission for the [Competition Name] Hackathon 2025.
