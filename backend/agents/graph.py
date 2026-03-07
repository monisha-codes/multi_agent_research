from langgraph.graph import StateGraph
from typing import TypedDict

from agents.planner_agent import planner_agent
from agents.research_agent import research_agent

class AgentState(TypedDict):
    question: str
    plan: str
    research_result: str


def build_graph():

    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", research_agent)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "researcher")

    graph.set_finish_point("researcher")

    return graph.compile()


def run_agents(question: str):
    app = build_graph()

    result = app.invoke({"question": question})

    return result