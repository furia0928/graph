from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.graph.conversation_state import ChatState
import json
from dotenv import load_dotenv
load_dotenv()

def summarize_conversation(state: ChatState, config: dict):
    recent_history = state.history[-3:] if len(state.history) >= 3 else state.history
    formatted_history = []
    for chat in recent_history:
        if chat.get("type") == "human":
            formatted_history.append({"user": chat.get("content", "")})
        elif chat.get("type") == "ai":
            formatted_history.append({"assistant": chat.get("content", "")})
    history_json = json.dumps(formatted_history, ensure_ascii=False)
    prompt = (
        "다음 대화 내용을 기반으로 새로운 대화 요약을 만들어줘.\n"
        f"기존 요약: {state.summary}\n\n"
        "최근 대화 (리스트 형식):\n"
        f"{history_json}\n\n"
        "새로운 요약:"
    )
    prompt_template = ChatPromptTemplate.from_messages([
        {"role": "system", "content": "너는 대화 요약 전문가야."},
        {"role": "user", "content": prompt}
    ])
    llm = ChatOpenAI(model="gpt-4o", temperature=0.5, max_tokens=150)
    response = llm.invoke(prompt_template.format_messages())
    print(response.content)
    new_summary = response.content.strip()
    return {"summary": new_summary}
