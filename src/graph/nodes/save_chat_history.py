import os
import datetime
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

def save_chat_history(state: ChatState, config: dict):
    chat_id = config["configurable"]["chat_id"]
    member_id = config["configurable"]["member_id"]

    now = datetime.datetime.utcnow()
    question_doc = {
        "member_id": member_id,
        "chat_id": chat_id,
        "type": "human",
        "contents": state.question,
        "registration_dt": now,
        "update_dt": now,
        "status": "active"
    }

    now_gen = now + datetime.timedelta(microseconds=1000)
    generation_doc = {
        "member_id": member_id,
        "chat_id": chat_id,
        "type": "ai",
        "contents": state.generation,
        "registration_dt": now_gen,
        "update_dt": now_gen,
        "status": "active"
    }

    chat_collection.insert_one(question_doc)
    chat_collection.insert_one(generation_doc)

    summary_doc = {
        "member_id": member_id,
        "chat_id": chat_id,
        "summary": state.summary,
        "registration_dt": now_gen,
        "update_dt": now_gen,
        "status": "active"
    }

    summary_collection.update_one(
        {"member_id": member_id, "chat_id": chat_id},
        {"$set": summary_doc},
        upsert=True
    )

    return state