from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from src.graph.conversation_state import ChatState
from src.graph.utils import convert_conversation_docs_to_messages

from dotenv import load_dotenv
load_dotenv()

def generate(state: ChatState):

    history_messages = convert_conversation_docs_to_messages(state.history)
    print("history_messages", history_messages)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "아래 정보를 참고하여 사용자의 질문에 대한 최종 응답을 생성해줘.\n\n"),
        ("system", "기존 요약: {summary}"),
        MessagesPlaceholder(variable_name="history", n_messages=4),
        ("human", "{question}"),
    ])
    print("generate prompt: ", prompt)
    formatted_messages = prompt.format_messages(
        summary=state.summary,
        question=state.question,
        history=history_messages
    )
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7, max_tokens=200)
    response = llm.invoke(formatted_messages)
    response_text = response.content.strip() if response and hasattr(response, "content") else "죄송합니다. 답변을 생성할 수 없습니다."
    return {"generation": response_text}
