from src.graph.agent import agent


def process_chat(chat_request):
    # 요청 데이터에서 필요한 정보 추출
    inputs = {
        "question": chat_request.question,
        "member_id": chat_request.member_id,
        "chat_id": chat_request.chat_id,
    }
    config = {
        "configurable": {"chat_id": chat_request.chat_id, "member_id": chat_request.member_id},
        "recursion_limit": 10
    }

    print(config)
    # 에이전트 호출
    result = agent.invoke(inputs, config=config)
    print(result)

    # 결과 가공 (필요에 따라 수정)
    return {
        "chat_id": chat_request.chat_id,
        "member_id": chat_request.member_id,
        "generation": result.get("generation", "결과가 없습니다.")
    }
