from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from src.graph.conversation_state import ChatState
from dotenv import load_dotenv

load_dotenv()

def generate(state: ChatState):
    print("generate", state)

    formatted_history = []
    for chat in state.history:
        role = "user" if chat.get("type") == "user" else "assistant"
        content = chat.get("contents", "")
        formatted_history.append(f"{role}: {content}")
    history_str = "\n".join(formatted_history)

    print("history_str: ", history_str)
    prompt = (
        "아래 정보를 참고하여 사용자의 질문에 대한 최종 응답을 생성해줘.\n\n"
        f"사용자 질문: {state.question}\n\n"
        f"기존 대화 요약: {state.summary}\n\n"
        f"최근 대화 내역 (최대 3개): {history_str}\n\n"
        "최종 응답:"
    )

    prompt_template = ChatPromptTemplate.from_messages([
        {"role": "system", "content": "너는 전문적인 조언자이자 도움을 주는 챗봇이다."},
        {"role": "user", "content": prompt}
    ])
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7, max_tokens=200)
    response = llm.invoke(prompt_template.format_messages())
    response_text = response.content.strip() if response and hasattr(response, "content") else "죄송합니다. 답변을 생성할 수 없습니다."
    return {"generation": response_text}
