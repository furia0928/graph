from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from src.graph.conversation_state import ChatState
from src.graph.utils import convert_conversation_docs_to_messages

from dotenv import load_dotenv
load_dotenv()

def summarize_conversation(state: ChatState, config: dict):
    recent_history = state.history[:2]

    history_messages = convert_conversation_docs_to_messages(recent_history)
    print("summarize_conversation history_messages", history_messages)
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "제공된 대화 내용을 점진적으로 요약하여 이전 요약에 추가하고, 새로운 요약을 생성하세요.\n\n"
         "예제\n"
         "현재 요약:\n"
         "사용자는 AI에게 인공지능에 대한 의견을 묻습니다. AI는 인공지능이 긍정적인 영향을 미친다고 생각합니다.\n\n"
         "새로운 대화 내용:\n"
         "사용자: 왜 인공지능이 긍정적인 영향을 미친다고 생각하나요?\n"
         "AI: 인공지능은 인간이 잠재력을 최대한 발휘할 수 있도록 돕기 때문입니다.\n\n"
         "새로운 요약:\n"
         "사용자는 AI에게 인공지능에 대한 의견을 묻습니다. "
         "AI는 인공지능이 긍정적인 영향을 미친다고 생각하며, 이는 인간이 잠재력을 최대한 발휘할 수 있도록 돕기 때문입니다.\n"
         "예제 끝.\n"),
        ("system", "사용자에 대한 정보는 매우 중요하니 꼭 기억해두어라."),
        ("system", "이전 요약:\n{summary}\n"),
        MessagesPlaceholder(variable_name="history"),
        ("system",
         "새로운 요약:\n"
         "이전 요약과 새로운 대화 내용을 바탕으로 간결하고 논리적인 업데이트된 요약을 생성하세요. "
         "핵심 정보를 유지하면서 중복된 내용을 제거하세요."),

        ("human", "업데이트된 요약을 제공하세요."),
    ])

    formatted_messages = prompt.format_messages(
        summary=state.summary,
        history=history_messages
    )
    print("summarize_conversation prompt: ", formatted_messages)

    llm = ChatOpenAI(model="gpt-4o", temperature=0.5, max_tokens=400)
    response = llm.invoke(formatted_messages)
    print("summarize_conversation", response.content)
    new_summary = response.content.strip()
    return {"summary": new_summary}
