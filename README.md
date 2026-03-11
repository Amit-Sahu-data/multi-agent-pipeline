# Multi-Agent Research Pipeline 🤖

An automated research pipeline where 3 specialized AI agents 
work together to research any topic and produce a professional email.

## How It Works
```
User enters topic
      ↓
Agent 1 (Researcher) → researches the topic in depth
      ↓
Agent 2 (Summarizer) → condenses research into clear summary
      ↓
Agent 3 (Email Writer) → writes professional email from summary
      ↓
Final email displayed on Streamlit UI
```

## Agents

- **Researcher Agent** — uses LLM knowledge to generate detailed research notes with statistics and insights
- **Summarizer Agent** — condenses research into 3-4 clear paragraphs
- **Email Writer Agent** — transforms summary into a professional ready-to-send email

## Tech Stack

- LangGraph + LangChain — agent framework
- Groq (LLaMA 3.1) — free LLM
- Streamlit — web UI
- Python-dotenv — environment management

## How to Run

1. Clone the repo
2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate
3. Install libraries
   pip install -r requirements.txt
4. Create .env file with your keys
   GROQ_API_KEY=your_key_here
5. Run the app
   streamlit run app.py

## Project Structure

- researcher.py — Agent 1: researches topic
- summarizer.py — Agent 2: summarizes research  
- email_writer.py — Agent 3: writes email
- pipeline.py — connects all 3 agents
- app.py — Streamlit UI