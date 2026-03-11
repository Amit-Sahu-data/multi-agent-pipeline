# summarizer.py
# Agent 2: Takes research notes and writes a clean summary

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Initialize
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def summarize_research(research_notes: str, topic: str) -> str:
    print(f"\nSummarizer: Summarizing research on '{topic}'...")

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert summarizer.
Your job is to take detailed research notes and create a clear, 
concise summary that captures the most important points.

Rules:
- Keep summary to 3-4 paragraphs maximum
- Start with the most important insight
- Include key numbers and statistics
- Use simple, clear language
- End with a conclusion or outlook"""),
        ("human", f"Topic: {topic}\n\nResearch Notes:\n{research_notes}\n\nWrite a clear concise summary.")
    ])

    chain = prompt | llm
    response = chain.invoke({})

    print("Summarizer: Done!")
    return response.content

# Test
if __name__ == "__main__":
    # Fake research notes for testing
    test_notes = """
    - AI agents are growing rapidly in 2025
    - 88% of executives plan to increase AI budgets
    - Agentic RAG is a major trend
    - Multi-agent systems are being adopted in enterprise
    - AI agents can reduce costs by up to 50%
    - LangGraph and CrewAI are leading frameworks
    """

    result = summarize_research(test_notes, "AI agents trends 2025")
    print("\n" + "="*50)
    print("SUMMARY OUTPUT:")
    print("="*50)
    print(result)