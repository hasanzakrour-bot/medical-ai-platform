from .retriever import retrieve_context
from .llm_engine import generate_answer

def rag_answer(question: str) -> str:
    context = retrieve_context(question)
    answer = generate_answer(context, question)
    return answer