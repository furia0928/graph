import graphviz


def visualize_graph():
    dot = graphviz.Digraph(format="png")
    print(dot)

    # ✅ 노드 추가
    dot.node("START", shape="oval")
    dot.node("get_chat_history", shape="box")
    dot.node("route_query", shape="diamond")
    dot.node("vector_search", shape="box")
    dot.node("web_search", shape="box")
    dot.node("generate", shape="ellipse")
    dot.node("save_chat_history", shape="parallelogram")
    dot.node("END", shape="oval")

    # ✅ 엣지 추가
    dot.edge("START", "get_chat_history")
    dot.edge("get_chat_history", "route_query")
    dot.edge("route_query", "vector_search", label="search")
    dot.edge("route_query", "generate", label="direct_answer")
    dot.edge("vector_search", "web_search", label="no_docs_found")
    dot.edge("vector_search", "generate", label="docs_found")
    dot.edge("web_search", "generate")
    dot.edge("generate", "save_chat_history")
    dot.edge("save_chat_history", "END")

    return dot


# ✅ 그래프 시각화 실행
dot = visualize_graph()
dot.render("langgraph_state_graph", view=True)
