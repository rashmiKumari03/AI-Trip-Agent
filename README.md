# 🌍 TripSathi AI — Intelligent Travel Planning Assistant

TripSathi AI is a multi-agent travel planning application that helps users design personalized journeys for vacations, business trips, and explorations.

Built with **CrewAI** and **Streamlit**, the app collects user preferences through a modern dark-themed interface and generates:

- Destination recommendations  
- Detailed city insights  
- Structured daily itineraries  
- Clear budget overviews  

All in one place.

---

## 🚩 Problem Statement

Planning a trip usually requires switching between many websites and tools.

Travelers often struggle with:

- Choosing the right destination  
- Matching plans to their travel purpose  
- Organizing daily schedules  
- Understanding budget expectations  
- Coordinating dates and trip length  
- Balancing comfort, pace, and logistics  

This makes travel planning slow, fragmented, and stressful.

---

## 💡 How TripSathi AI Solves It

TripSathi AI centralizes the entire planning process.

Users simply provide:

- Arrival and return dates  
- Travel purpose  
- Interests  
- Travel pace  
- Budget level  
- Number of travelers  
- Accommodation type  
- Food preferences  
- Special notes  

A team of specialized AI agents collaborates to generate:

- Recommended destinations  
- Cultural and travel insights  
- Day-by-day itineraries  
- Budget breakdowns  

The result is a professional travel plan tailored to the user.

---

## ✨ Key Features

- 🌐 Destination recommendations based on preferences  
- 📅 Automatic trip duration calculation from selected dates  
- 🎯 Personalized travel planning  
- 🗺️ City research and local insights  
- 🗓️ Daily itinerary generation  
- 💼 Budget overview by category  
- 🤖 Multi-agent coordination using CrewAI  
- 🎨 Dark neon-styled Streamlit interface  
- 🖼️ Auto-rotating hero image slider  
- 🔐 Secure LLM gateway configuration  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- CrewAI  
- LangChain  
- uv  
- python-dotenv  
- HTML & CSS styling  
- LLM Gateway 

---

## 📁 Project Structure
```
AI_TRIP_AGENT/
│
├── .venv/
│
├── config/
│   ├── __init__.py
│   └── llm_config.py
│
├── src/
│   ├── __init__.py
│   ├── agents.py
│   ├── tasks.py
│   └── crew.py
│
├── test/
│   ├── __init__.py
│   └── test_llm.py
│
├── .env
├── .gitignore
├── app.py
├── LICENSE
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## ⚡ Installation & Setup (Using uv)

### 1️⃣ Install uv

```bash
pip install uv
```

Verify:

```bash
uv --version
```

---

### 2️⃣ Initialize Project

```bash
uv init
```

---

### 3️⃣ Create Virtual Environment

```bash
uv venv
```

Activate:

**Windows**
```bash
.venv\Scripts\activate
```

**Mac / Linux**
```bash
source .venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## 📦 Add Dependencies to pyproject.toml

To sync packages into TOML:

```bash
uv add streamlit crewai langchain python-dotenv
```

This updates:

- pyproject.toml  
- uv.lock  

---

## 🔑 Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://api.euron.one/api/v1/euri
```

---

## 🧪 Test LLM Connection

Before launching the UI:

```bash
python test_llm.py
```

Expected output:

```
LLM connection OK
```

---

## ▶ Run the Application

```bash
streamlit run main.py
```

Open:

```
http://localhost:8501
```

---

## 🖼️ Screenshots

Add screenshots inside an `images/` folder:

### Home Screen

```
images/home.png
```

### Generated Plan

```
images/results.png
```

---

## 📊 Results

TripSathi AI generates:

- Three destination suggestions  
- Detailed city insights  
- Structured itineraries  
- Budget summaries  
- Personalized recommendations  

Displayed in an interactive dashboard.

---

## 🚀 Why This Project Matters

- Demonstrates real-world multi-agent AI systems  
- Clean UI design with Streamlit  
- Practical problem solving  
- Modular architecture  
- Ideal for portfolios and academic submissions  

---