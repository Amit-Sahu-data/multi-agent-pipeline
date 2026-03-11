# email_writer.py
# Agent 3: Takes summary and writes a professional email

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Initialize
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

def write_email(summary: str, topic: str, recipient: str = "Team") -> str:
    print(f"\nEmail Writer: Writing email on '{topic}'...")

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a professional email writer.
Your job is to take a research summary and write a 
clear, professional email sharing the key insights.

Rules:
- Start with a clear subject line
- Keep it professional but conversational
- Highlight the most important insights
- Include key numbers and statistics
- End with a clear call to action
- Keep it concise — busy people read this"""),
        ("human", f"""Write a professional email to {recipient} about: {topic}

Based on this summary:
{summary}

Format:
Subject: [subject line]

[email body]""")
    ])

    chain = prompt | llm
    response = chain.invoke({})

    print("Email Writer: Done!")
    return response.content

# Test
if __name__ == "__main__":
    test_summary = """
    AI agents are growing rapidly in 2025. 88% of executives 
    plan to increase AI budgets. Agentic RAG and multi-agent 
    systems are major trends. AI agents can reduce costs by 
    up to 50%. LangGraph and CrewAI are leading frameworks.
    """

    result = write_email(test_summary, "AI agents trends 2025", "Leadership Team")
    print("\n" + "="*50)
    print("EMAIL OUTPUT:")
    print("="*50)
    print(result)