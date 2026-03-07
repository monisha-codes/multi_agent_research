# Mock MCP tool

def mock_web_search(query: str) -> str:
    fake_results = {
        "capital of france": "The capital of France is Paris.",
        "capital of germany": "The capital of Germany is Berlin.",
    }

    return fake_results.get(
        query.lower(),
        f"No results found for '{query}', but this is a mock response."
    )