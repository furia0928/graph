from app.chat_state import ChatState


def vector_search(state: ChatState):
    return {"documents": state.documents}