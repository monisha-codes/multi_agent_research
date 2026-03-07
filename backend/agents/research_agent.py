from mcp.mcp_server import mock_web_search

def research_agent(state):
    plan = state["plan"]

    result = mock_web_search(plan)

    return {**state, "research_result": result}