from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.graph.conversation_state import ChatState
import json
from dotenv import load_dotenv
load_dotenv()

def summarize_conversation(state: ChatState, config: dict):
    recent_history = state.history[-2:] if len(state.history) >= 3 else state.history
    formatted_history = []
    for chat in recent_history:
        role = "user" if chat.get("type") == "user" else "assistant"
        content = chat.get("contents", "")
        formatted_history.append(f"{role}: {content}")
    history_str = "\n".join(formatted_history)
    prompt = (
        "다음 대화 내용을 기반으로 새로운 대화 요약을 만들어줘.\n"
        f"기존 요약: {state.summary}\n\n"
        "최근 대화 (리스트 형식):\n"
        f"{history_str}\n\n"
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
