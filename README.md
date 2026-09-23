# 🤖 AI Customer Support Chatbot — AutoGen Agent Teams

An **AI-powered enterprise customer support chatbot** built with **Python, AutoGen Agent Teams, OpenAI, and Streamlit**.

The application uses a **Manager Agent** to understand the user's question and route it to one of five specialized department agents:

* 💻 IT
* 💰 Finance
* 👥 HR
* 🏨 Hospitality
* 🔐 Security

The selected department agent then generates the response and returns it to the user through a Streamlit chat interface.

---

## 🚀 Project Overview

Traditional customer-support systems often require users to know which department they should contact.

This project introduces a **multi-agent architecture** where the user simply asks a question.

For example:

```text
User:
I lost my company access badge.

        ↓

Manager Agent
        ↓
SECURITY

        ↓

Security Agent
        ↓

Your access badge has been lost...
Please contact the security desk...
```

The user does not need to manually select a department.

---

# 🏗️ Architecture

```text
                         ┌───────────────────────┐
                         │    Streamlit UI       │
                         │       Chatbot         │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │    Manager Agent      │
                         │                       │
                         │  Intent Detection &   │
                         │      Routing          │
                         └───────────┬───────────┘
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                      │
              ▼                      ▼                      ▼
        ┌──────────┐          ┌──────────┐          ┌──────────┐
        │ IT Agent │          │ Finance  │          │ HR Agent │
        │          │          │  Agent   │          │          │
        └──────────┘          └──────────┘          └──────────┘
              │                      │                      │
              │              ┌───────┴────────┐             │
              │              │                │             │
              ▼              ▼                ▼             ▼
         IT Support      Hospitality       Security      HR Support
                           Agent              Agent
              │              │                │             │
              └──────────────┴────────────────┴─────────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │ Final AI Response│
                            └────────┬─────────┘
                                     │
                                     ▼
                                  User
```

---

# ✨ Features

### 🤖 Multi-Agent Architecture

Uses AutoGen Agent Teams with:

* 1 Manager Agent
* 5 Department Agents

```text
Manager Agent
     │
     ├── IT Agent
     ├── Finance Agent
     ├── HR Agent
     ├── Hospitality Agent
     └── Security Agent
```

---

### 🧠 Intelligent Routing

The Manager Agent analyzes the user's question and determines the appropriate department.

Example:

```text
"My VPN is not working"

        ↓

Manager Agent

        ↓

IT

        ↓

IT Agent
```

---

### 💻 IT Support

Handles questions related to:

* Laptop
* Desktop
* VPN
* Network
* Wi-Fi
* Software
* Applications
* Email
* Outlook
* Password
* Hardware
* Printers

Example:

```text
My laptop VPN is not connecting.
```

---

### 💰 Finance Support

Handles:

* Salary
* Payroll
* Expenses
* Travel expenses
* Reimbursement
* Invoices
* Payments
* Purchase orders
* Budget

Example:

```text
How can I claim my travel expenses?
```

---

### 👥 HR Support

Handles:

* Leave
* Vacation
* Employee benefits
* Attendance
* Recruitment
* Onboarding
* Training
* Performance
* HR policies

Example:

```text
How many vacation days can I take?
```

---

### 🏨 Hospitality Support

Handles:

* Meeting rooms
* Conference rooms
* Cafeteria
* Food
* Catering
* Guest services
* Office facilities
* Events
* Facility booking

Example:

```text
I need to book a meeting room.
```

---

### 🔐 Security Support

Handles:

* Security badges
* Access cards
* Building access
* Visitor access
* Lost badges
* Security incidents
* Physical security
* Emergency security

Example:

```text
I lost my company access badge.
```

---

# 🛠️ Technology Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Application development   |
| AutoGen           | Multi-agent orchestration |
| AutoGen AgentChat | Agent implementation      |
| OpenAI            | LLM / reasoning           |
| Streamlit         | Chatbot UI                |
| python-dotenv     | Environment configuration |
| asyncio           | Async execution           |

---

# 📁 Project Structure

```text
customer-support-agent-in-autogen/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── agents/
│   ├── __init__.py
│   ├── manager_agent.py
│   ├── it_agent.py
│   ├── finance_agent.py
│   ├── hr_agent.py
│   ├── hospitality_agent.py
│   └── security_agent.py
│
└── services/
    ├── __init__.py
    └── support_team.py
```

---

# 🔄 Request Processing Flow

The application follows this workflow:

```text
1. User enters question
          │
          ▼
2. Streamlit receives question
          │
          ▼
3. Manager Agent analyzes question
          │
          ▼
4. Department identified
          │
          ├──── IT
          ├──── Finance
          ├──── HR
          ├──── Hospitality
          └──── Security
          │
          ▼
5. Selected Department Agent
          │
          ▼
6. Department Agent generates response
          │
          ▼
7. Response displayed in Streamlit
```

---

# 🧩 Agent Responsibilities

## Manager Agent

The Manager Agent does **not** answer the user's question.

Its responsibility is:

```text
User Question
     ↓
Intent Detection
     ↓
Department Classification
     ↓
Route Request
```

It returns one of:

```text
IT
FINANCE
HR
HOSPITALITY
SECURITY
```

---

## Department Agents

Each specialist agent has its own system instructions.

### IT Agent

```text
Technical Support
      ↓
Laptop
VPN
Network
Software
Email
Hardware
```

### Finance Agent

```text
Finance Support
      ↓
Payroll
Expenses
Invoices
Payments
Reimbursement
```

### HR Agent

```text
HR Support
      ↓
Leave
Benefits
Attendance
Recruitment
Onboarding
```

### Hospitality Agent

```text
Hospitality Support
      ↓
Meeting Rooms
Cafeteria
Facilities
Events
Guest Services
```

### Security Agent

```text
Security Support
      ↓
Badges
Access
Visitors
Security Incidents
Physical Security
```

---

# 🔐 Environment Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

Never commit the `.env` file to GitHub.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-support-agent-in-autogen.git
```

```bash
cd customer-support-agent-in-autogen
```

---

## 2. Create virtual environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Example `requirements.txt`:

```text
autogen-agentchat
autogen-ext[openai]
streamlit
python-dotenv
```

---

# 🔑 Configure OpenAI API Key

Create:

```text
.env
```

Add:

```env
OPENAI_API_KEY=your_openai_api_key
```

The application reads the API key using:

```python
from dotenv import load_dotenv

load_dotenv()
```

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 💬 Example Conversations

## Example 1 — IT

**User**

```text
My VPN is not working.
```

**Manager Agent**

```text
IT
```

**Response**

```text
🏢 Routed to IT Department

The IT Support Agent will help troubleshoot
your VPN connectivity issue.
```

---

## Example 2 — Finance

**User**

```text
How do I submit my travel expenses?
```

Routing:

```text
Manager Agent
      ↓
FINANCE
      ↓
Finance Agent
```

---

## Example 3 — HR

**User**

```text
How many vacation days can I take?
```

Routing:

```text
Manager Agent
      ↓
HR
      ↓
HR Agent
```

---

## Example 4 — Hospitality

**User**

```text
I need to book a meeting room.
```

Routing:

```text
Manager Agent
      ↓
HOSPITALITY
      ↓
Hospitality Agent
```

---

## Example 5 — Security

**User**

```text
I lost my company access badge.
```

Routing:

```text
Manager Agent
      ↓
SECURITY
      ↓
Security Agent
```

---

# 🐛 Routing Logic

The application uses **exact department matching**.

```python
if routing == "IT":
    selected_agent = self.it_agent

elif routing == "FINANCE":
    selected_agent = self.finance_agent

elif routing == "HR":
    selected_agent = self.hr_agent

elif routing == "HOSPITALITY":
    selected_agent = self.hospitality_agent

elif routing == "SECURITY":
    selected_agent = self.security_agent
```

This is important because substring matching such as:

```python
if "IT" in routing:
```

can incorrectly match:

```text
HOSPITALITY
```

because:

```text
HOSPITALITY
        ^^
        IT
```

The project therefore uses exact matching.

---

# ⚡ Async Event Loop Handling

Because Streamlit reruns the Python application when the user interacts with the UI, the application creates and closes the AutoGen model client inside a single async lifecycle.

```text
Streamlit
    │
    ▼
asyncio.run()
    │
    ▼
Create OpenAI Client
    │
    ▼
Create Agent Team
    │
    ▼
Manager Agent
    │
    ▼
Department Agent
    │
    ▼
Response
    │
    ▼
Close OpenAI Client
```

This avoids errors such as:

```text
RuntimeError: Event loop is closed
```

---

# 🎨 Streamlit UI

The application provides:

* Chat interface
* Chat history
* Department routing information
* Department descriptions
* Loading indicator
* Error handling
* AI assistant responses

Example:

```text
┌──────────────────────────────────────────────┐
│ 🤖 Company AI Customer Support               │
├──────────────────────────────────────────────┤
│                                              │
│ 👤 I lost my company access badge            │
│                                              │
│ 🤖 🏢 Routed to Security Department          │
│                                              │
│    Please contact the security desk...       │
│                                              │
├──────────────────────────────────────────────┤
│ Ask your company support question...         │
└──────────────────────────────────────────────┘
```

---

# 🔮 Future Enhancements

This project can be extended into a more complete enterprise AI architecture.

### Phase 1 — Current

```text
Manager Agent
     ↓
5 Department Agents
     ↓
Streamlit
```

### Phase 2 — Conversation Memory

Add:

```text
Conversation History
        ↓
Manager + Department Agent
```

The chatbot can maintain context across multiple questions.

---

### Phase 3 — RAG

Add department-specific knowledge bases:

```text
                    Manager
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
    IT RAG         Finance RAG       HR RAG
       │               │               │
       ▼               ▼               ▼
   IT Documents    Finance Docs     HR Policies
```

Additional RAG sources can include:

* PDF
* Word documents
* Excel
* Company policies
* FAQs
* SOPs
* Internal documentation

---

### Phase 4 — Tools and APIs

Agents can be connected to enterprise systems.

```text
IT Agent
   └── Ticketing API

Finance Agent
   └── Expense API

HR Agent
   └── Employee/Leave API

Hospitality Agent
   └── Room Booking API

Security Agent
   └── Access Management API
```

---

### Phase 5 — Guardrails

Add input and output guardrails:

```text
User
 ↓
Input Guardrail
 ↓
Manager
 ↓
Department Agent
 ↓
Output Guardrail
 ↓
User
```

Guardrails can help detect:

* Prompt injection
* Sensitive information
* Unsafe requests
* Off-topic questions
* Confidential data exposure

---

### Phase 6 — Evaluation

Evaluate the multi-agent system using metrics such as:

```text
Routing Accuracy
Response Relevance
Answer Correctness
Groundedness
Response Quality
```

Example:

```text
Question
   ↓
Expected Department
   ↓
Actual Department
   ↓
Evaluation
```

---

### Phase 7 — Human Escalation

Add human-in-the-loop support:

```text
User
 ↓
Manager
 ↓
Department Agent
 ↓
Confidence Check
 ↓
 ┌───────────────┐
 │               │
High           Low
 │               │
 ▼               ▼
Answer       Human Agent
```

---

# 🏢 Enterprise Architecture — Future

The complete architecture can eventually become:

```text
                         ┌───────────────────┐
                         │    Streamlit UI   │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │    Manager Agent  │
                         └─────────┬─────────┘
                                   │
       ┌───────────────────────────┼───────────────────────────┐
       │                           │                           │
       ▼                           ▼                           ▼
   IT Agent                   Finance Agent                 HR Agent
       │                           │                           │
       ▼                           ▼                           ▼
    IT RAG                     Finance RAG                  HR RAG
       │                           │                           │
       ▼                           ▼                           ▼
  IT APIs/Tools              Finance APIs                HR APIs
       │                           │                           │
       └───────────────────────────┼───────────────────────────┘
                                   │
                         ┌─────────┴─────────┐
                         │                   │
                         ▼                   ▼
                 Hospitality Agent     Security Agent
                         │                   │
                         ▼                   ▼
                    Hospitality RAG      Security RAG
                         │                   │
                         └─────────┬─────────┘
                                   ▼
                          Output Guardrails
                                   │
                                   ▼
                            Human Escalation
                                   │
                                   ▼
                                User
```

---

# 📊 Learning Objectives

This project demonstrates practical concepts in:

* Generative AI
* Multi-Agent Systems
* AutoGen
* Agent Teams
* Agent Routing
* LLM-based Intent Classification
* Specialized AI Agents
* Async Python
* Streamlit
* Enterprise AI Architecture

---

# 🎯 Key Takeaways

This project demonstrates how multiple specialized AI agents can collaborate to provide a single customer-support experience.

Instead of building one large chatbot:

```text
❌ One Large Agent
```

we use:

```text
             Manager Agent
                   │
       ┌───────────┼───────────┐
       │           │           │
      IT        Finance       HR
       │           │           │
 Hospitality    Security
```

Each agent has a clearly defined responsibility.

---

# 🚀 Future Technology Stack

The project can eventually evolve into:

```text
Python
   +
AutoGen
   +
OpenAI
   +
Streamlit
   +
LangChain
   +
FAISS
   +
RAG
   +
Guardrails
   +
Evaluation
   +
FastAPI
   +
Docker
```

This creates a strong foundation for an **enterprise multi-agent customer-support platform**.

---

# 👨‍💻 Author

**Dinesh Kumar**

AI & Java Full Stack Developer | GenAI | Agentic AI | RAG | Java | Spring Boot

🔗 LinkedIn: **[www.linkedin.com/in/dinesh-ai-man](http://www.linkedin.com/in/dinesh-ai-man)**

---

# ⭐ If you find this project useful

Feel free to:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐛 Report issues
* 💡 Suggest improvements
* 🤝 Contribute

---

## 📌 Project Keywords

```text
AutoGen
AutoGen Agent Teams
Multi Agent AI
Agentic AI
Generative AI
OpenAI
Python
Streamlit
AI Customer Support
AI Agents
LLM
Agent Routing
Enterprise AI
Conversational AI
Intelligent Automation
```
