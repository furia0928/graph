from app.chat_state import ChatState


def decide_to_web_search(state: ChatState):
    return "generate" if state.documents else "web_search"