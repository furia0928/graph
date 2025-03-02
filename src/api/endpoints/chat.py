from fastapi import APIRouter, HTTPException
from src.api.models import ChatRequest, ChatResponse
from src.api.services import process_chat

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Graph API is running."}

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response = process_chat(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
