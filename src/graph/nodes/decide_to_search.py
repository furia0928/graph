from src.graph.conversation_state import ChatState


def decide_to_search(state: ChatState):
    return "generate" if state.documents else "vector_search"