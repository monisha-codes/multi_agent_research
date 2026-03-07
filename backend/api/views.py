from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Conversation
from agents.graph import run_agents

@api_view(["POST"])
def ask_question(request):
    question = request.data.get("question")

    result = run_agents(question)

    answer = result["research_result"]

    Conversation.objects.create(
        question=question,
        answer=answer
    )

    return Response({
        "planner_output": result["plan"],
        "research_output": result["research_result"],
        "final_answer": answer
    })