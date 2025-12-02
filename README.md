# 🎓 EduPath
### AI-Powered Educational Orchestrator built with Google ADK, Gemini 1.5, and FastAPI

EduPath Navigator Enterprise is a next-generation **autonomous multi-agent educational intelligence system** that automates research, grading, planning, and communication in the academic lifecycle.  
Built using the **Google Agent Development Kit (ADK)** and **Gemini 1.5**, it functions as an always-on:

- 🔍 Opportunity Finder  
- 📝 Academic Grader  
- 📚 Personal Study Planner  
- 📢 Communication Assistant  
- 📊 Classroom Insights Engine

This project solves the *Time & Discovery Crisis* in modern education by enabling instant, scalable, AI-driven academic support.

---

## 🚀 Key Highlights (SEO-Optimized)
- AI Education Assistant
- Autonomous Multi-Agent Architecture
- Gemini 1.5 + Google ADK
- Real-time student analytics
- FastAPI-powered backend
- Automated homework grading & study plan creation
- Human-in-the-loop teacher verification
- Long-term student memory with SQLite

---
<img width="1024" height="1024" alt="Gemini_Generated_Image_lrmx43lrmx43lrmx" src="https://github.com/user-attachments/assets/9f944e03-ec02-410e-8c2b-f3e6b0c44d74" />


# 🏆 Project Overview

EduPath Navigator Enterprise automates the full educational support workflow:

### 1. Discovery  
Real-time scanning for scholarships, competitions, internships, and academic opportunities using intelligent search agents.

### 2. Assessment  
Automated homework grading, code execution, and detection of student weaknesses.

### 3. Planning  
An iterative AI-driven study plan generator with teacher approval.

### 4. Communication  
Daily performance summaries, parent reports, and classroom-wide insights for teachers.

---

# 🧠 Architecture Overview

<img width="2403" height="1752" alt="Mermaid Chart - Create complex, visual diagrams with text -2025-12-01-091740" src="https://github.com/user-attachments/assets/25a0bfef-b18d-4b73-b28d-181b35ff6dda" />


---

# 🤖 Agent Team & Roles

| Agent | Role | Model | Key Tools |
|-------|------|--------|----------|
| Scout | Researcher | Gemini 1.5 Flash | google_search |
| Tutor | Academic Grader | Gemini 1.5 Flash | code_execution, log_student_weakness |
| Planner | Study Strategist | Gemini 1.5 Flash | – |
| Critic | Quality Control | Gemini 1.5 Flash | request_teacher_approval |
| Liaison | Communication & Reports | Gemini 1.5 Pro | check_class_alerts, get_student_history |

---

# ✨ Features

### ⚡ Parallel Execution Engine  
Scout + Tutor run simultaneously.

### 🔄 Iterative Planning Loop  
Planner and Critic collaborate until teacher approval.

### 💾 Persistent Long-Term Memory  
SQLite-based memory bank.

### 🛠️ Custom MCP Tooling  
- log_student_weakness  
- check_class_trends  
- request_teacher_approval  

### 📉 Context Compaction System  
Automatic token optimization.

---

# 🛠️ Installation & Setup

## Prerequisites
- Python 3.10+
- Google API Key
- Git

## 1. Clone the Repository
```
git clone https://github.com/jjeni/edupath.git
cd edupath
```

## 2. Create a Virtual Environment
```
python -m venv venv
```
Windows:
```
venv\Scripts\activate
```
Mac/Linux:
```
source venv/bin/activate
```

## 3. Install Dependencies
```
pip install -r requirements.txt
```

## 4. Configure API Key
Windows:
```
set GOOGLE_API_KEY=your_actual_api_key_here
```
Mac/Linux:
```
export GOOGLE_API_KEY=your_actual_api_key_here
```

---

# 🏃‍♂️ Usage

Start the server:
```
python main.py
```
Open Swagger:
```
http://127.0.0.1:8000/docs
```

---

# 🧪 Example Queries

### Student Persona  
"Analyze my homework and weaknesses..."

### Parent Persona  
"Generate a performance report for my child."

### Teacher Persona  
"Run class analytics."

---

# 📂 Project Structure
```
edupath-navigator/
├── src/
│   ├── agents/
│   ├── core/
│   ├── tools/
│   └── workflow.py
├── main.py
├── requirements.txt
└── edupath_enterprise.db
```


