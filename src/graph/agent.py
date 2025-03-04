from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from src.graph.conversation_state import ChatState
from src.graph.nodes import *

class ConfigSchema(TypedDict):
    model: str
    chat_id : str
    member_id : str

# ✅ LangGraph 그래프 생성
graph = StateGraph(ChatState, config_schema=ConfigSchema)

# ✅ 노드 추가
graph.add_node("get_chat_history", get_chat_history)
graph.add_node("route_query", route_query)
graph.add_node("vector_search", vector_search)
graph.add_node("web_search", web_search)
graph.add_node("generate", generate)
graph.add_node("save_chat_history", save_chat_history)
graph.add_node("summarize_conversation", summarize_conversation)

# ✅ 엣지 추가
graph.add_edge(START, "get_chat_history")
graph.add_edge("get_chat_history", "route_query",)
graph.add_conditional_edges(
    "route_query",
    decide_to_search,
    {
        "vector_search": "vector_search",
        "generate": "generate"
    }
)
graph.add_conditional_edges(
    "vector_search",
    decide_to_web_search,
    {
        "web_search": "web_search",
        "generate": "generate"
    }
)
graph.add_edge("web_search", "generate")
graph.add_edge("generate", "summarize_conversation")
graph.add_edge("summarize_conversation", "save_chat_history")
graph.add_edge("save_chat_history", END)

# ✅ 컴파일
agent = graph.compile()
