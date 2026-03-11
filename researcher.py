# researcher.py
# Agent 1: Researches a topic using LLM knowledge

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Initialize
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

def research_topic(topic: str) -> str:
    print(f"\nResearcher: Researching '{topic}'...")

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert research assistant with deep knowledge 
across all domains. Your job is to provide comprehensive, well-structured 
research notes on any given topic.

Include:
- Key facts and statistics
- Current trends
- Important developments
- Expert insights
- Real numbers and data where possible

Format with clear sections and bullet points."""),
        ("human", f"Provide detailed research notes on: {topic}")
    ])

    chain = prompt | llm
    response = chain.invoke({})

    print("Researcher: Done!")
    return response.content

# Test
if __name__ == "__main__":
    result = research_topic("AI agents trends 2025")
    print("\n" + "="*50)
    print("RESEARCH OUTPUT:")
    print("="*50)
    print(result)