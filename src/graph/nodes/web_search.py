from src.graph.conversation_state import ChatState


def web_search(state: ChatState):
    return {"documents": state.documents}