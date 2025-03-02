from src.graph.conversation_state import ChatState


def decide_to_search(state: ChatState) -> str:
    return "generate" if state.search_decision == "direct" else "vector_search"
