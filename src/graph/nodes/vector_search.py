from src.graph.conversation_state import ChatState


def vector_search(state: ChatState):
    return {"documents": state.documents}