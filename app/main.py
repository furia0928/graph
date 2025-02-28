import sys
import logging
from app.graph import agent  # 에이전트 모듈 import


def main():
    # 테스트용 사용자 정보 및 질문
    member_id = "user_1"
    chat_id = "chat_1"
    question = "테스트 질문: Next.js에서 API 요청을 최적화하는 방법은?"

    inputs = {"question": question, "member_id": member_id, "chat_id": chat_id}
    config = {
        "configurable": {"chat_id": chat_id, "member_id": member_id},
        "recursion_limit": 10
    }

    try:
        response = agent.invoke(inputs, config=config)
        print("에이전트 응답:", response.get("generation", "결과가 없습니다."))
    except Exception as e:
        logging.error("에이전트 호출 중 오류 발생: %s", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
