from pydantic import BaseModel
from typing import List, Optional

class ChatState(BaseModel):
    question: str  # 사용자 질문
    generation: Optional[str] = None  # LLM 생성 응답 (기본값: None)
    documents: List[str] = []  # 웹 or 백터 검색 결과 (기본값: 빈 리스트)
    history: List[dict] = []  # 최근 대화 (기본값: 빈 리스트, 최대 갯수: 6개)
    summary: Optional[str] = ""  # 요약 (기본값: 빈 문자열)
