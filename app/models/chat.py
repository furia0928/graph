from pydantic import BaseModel

class ChatRequest(BaseModel):
    chat_id: str
    member_id: str
    question: str

class ChatResponse(BaseModel):
    chat_id: str
    member_id: str
    generation: str
