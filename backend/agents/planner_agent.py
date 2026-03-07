import ollama
import re

def planner_agent(state):
    question = state["question"]

    prompt = f"""
You are a planning assistant.

Convert the question into a short search query.

Return ONLY the search query.
Do not explain anything.

Question: {question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    plan = response["message"]["content"].strip()

    # Extract query if LLM adds quotes or extra text
    match = re.search(r'"(.*?)"', plan)

    if match:
        plan = match.group(1)

    return {**state, "plan": plan}