from app.graph import agent  # ✅ 직접 import

# ✅ 실행 예제
member_id = "user_1"
chat_id = "chat_1"
question = "Next.js에서 API 요청을 최적화하는 방법은?"

inputs = {"question": "안녕"}
response = agent.invoke(
    inputs,
    config={"configurable": {"chat_id": chat_id, "member_id": member_id}, "recursion_limit": 10},
)
print(response["generation"])
