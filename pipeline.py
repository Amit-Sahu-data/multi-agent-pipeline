# pipeline.py
# Connects all 3 agents in sequence using LangGraph

from langgraph.graph import StateGraph, END
from typing import TypedDict
from researcher import research_topic
from summarizer import summarize_research
from email_writer import write_email

# -----------------------------------------
# Step 1: Define the State
# State = data that flows between agents
# -----------------------------------------
class PipelineState(TypedDict):
    topic: str
    research: str
    summary: str
    email: str

# -----------------------------------------
# Step 2: Define each node (agent function)
# -----------------------------------------
def researcher_node(state: PipelineState) -> PipelineState:
    print("\n>>> Running Researcher Agent...")
    research = research_topic(state['topic'])
    return {"research": research}

def summarizer_node(state: PipelineState) -> PipelineState:
    print("\n>>> Running Summarizer Agent...")
    summary = summarize_research(state['research'], state['topic'])
    return {"summary": summary}

def email_writer_node(state: PipelineState) -> PipelineState:
    print("\n>>> Running Email Writer Agent...")
    email = write_email(state['summary'], state['topic'])
    return {"email": email}

# -----------------------------------------
# Step 3: Build the graph
# Graph = the pipeline connecting all agents
# -----------------------------------------
def build_pipeline():
    graph = StateGraph(PipelineState)

    # Add nodes
    graph.add_node("researcher", researcher_node)
    graph.add_node("summarizer", summarizer_node)
    graph.add_node("email_writer", email_writer_node)

    # Connect nodes in sequence
    graph.set_entry_point("researcher")
    graph.add_edge("researcher", "summarizer")
    graph.add_edge("summarizer", "email_writer")
    graph.add_edge("email_writer", END)

    return graph.compile()

# -----------------------------------------
# Step 4: Run the full pipeline
# -----------------------------------------
def run_pipeline(topic: str) -> dict:
    pipeline = build_pipeline()

    print(f"\nStarting pipeline for topic: '{topic}'")
    print("="*50)

    result = pipeline.invoke({"topic": topic})

    print("\n" + "="*50)
    print("PIPELINE COMPLETE!")
    print("="*50)

    return result

# Test
if __name__ == "__main__":
    result = run_pipeline("AI agents trends 2025")

    print("\n RESEARCH:")
    print(result['research'])
    print("\n SUMMARY:")
    print(result['summary'])
    print("\n EMAIL:")
    print(result['email'])