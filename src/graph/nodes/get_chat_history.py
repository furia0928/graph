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
        .sort("registration_dt", -1)
        .limit(4)
    )[::-1]

    print("latest_chats lengths: ", len(latest_chats))

    summary_data = summary_collection.find_one({"chat_id": chat_id})

    summary = summary_data["summary"] if summary_data else ""

    return {"history": latest_chats, "summary": summary}
