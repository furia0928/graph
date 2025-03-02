from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from src.graph.conversation_state import ChatState

# ✅ Pydantic 모델 정의 (응답을 'direct' 또는 'search'로 강제)
class QueryRoutingResponse(BaseModel):
    binary_score: str = Field(description="Decide if the question can be answered directly ('direct') or needs additional search ('search')")

def route_query(state: ChatState, config: dict):
    model = config["configurable"]["model"]
    print(model)
    llm = ChatOpenAI(model=model, temperature=0).with_structured_output(QueryRoutingResponse)

    # ✅ 프롬프트 구성
    prompt = ChatPromptTemplate.from_messages([
        ("system", "너는 AI 어시스턴트야. 사용자의 질문을 분석해서 네가 직접 답변할 수 있는지 판단해."),
        ("user", "질문: {question}"),
        ("system", "네가 바로 답할 수 있으면 'direct', 추가 정보가 필요하면 'search' 라고 응답해.")
    ])

    # ✅ 프롬프트에 질문 적용
    formatted_prompt = prompt.format_messages(question=state.question)

    # ✅ LLM 실행 (JSON 형식의 응답)
    response = llm.invoke(formatted_prompt)

    # ✅ JSON에서 결과 추출 (with_structured_output을 사용하므로 response.binary_score 이용)
    decision = response.binary_score.strip().lower()
    if decision not in ["direct", "search"]:
        decision = "search"  # ✅ 잘못된 응답 방지

    state.search_decision = decision  # ✅ ChatState에 검색 여부 저장

    return state
