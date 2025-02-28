from app.chat_state import ChatState


def generate(state: ChatState):
    # ✅ LLM 응답 생성 로직 (예제)
    response = "이건 예제 응답입니다."  # 실제 LLM 호출 필요

    if not response:  # ✅ 응답이 없을 경우 기본값 설정
        response = "죄송합니다. 답변을 생성할 수 없습니다."

    return {"generation": response}  # ✅ dict 반환
