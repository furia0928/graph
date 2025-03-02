import os
from pymongo import MongoClient
from src.graph.conversation_state import ChatState

# ✅ MongoDB 설정
MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = "chat_memory"
CHAT_COLLECTION = "conversations"  # 대화 기록 저장 컬렉션
SUMMARY_COLLECTION = "summaries"   # 요약 데이터 저장 컬렉션

# ✅ MongoDB 연결
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
chat_collection = db[CHAT_COLLECTION]
summary_collection = db[SUMMARY_COLLECTION]

def get_chat_history(state: ChatState, config: dict):
    chat_id = config["configurable"]["chat_id"]

    # ✅ 최신 대화 4개 가져오기
    latest_chats = list(
        chat_collection.find({"chat_id": chat_id})
        .sort("registration_dt", -1)  # 최신순 정렬
        .limit(4)
    )

    print("latest_chats: ", latest_chats)

    # ✅ 포맷팅 (사용자 메시지 & AI 응답 포함)
    formatted_history = []
    for chat in latest_chats:
        if chat.get("type") == "human":
            formatted_history.append({"user": chat.get("content", "")})
        elif chat.get("type") == "ai":
            formatted_history.append({"assistant": chat.get("content", "")})

    # ✅ 요약 데이터 가져오기 (chat_id 기반)
    summary_data = summary_collection.find_one({"chat_id": chat_id})
    summary = summary_data["summary"] if summary_data else ""

    print("history: ", formatted_history)
    print("summary: ", summary)

    return {"history": formatted_history, "summary": summary}
