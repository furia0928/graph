def convert_conversation_docs_to_messages(docs: list[dict]) -> list[tuple[str, str]]:
    messages = []
    for doc in docs:
        msg_type = doc.get("type", "").lower()
        content = doc.get("contents", "")
        if msg_type == "ai":
            messages.append(("ai", content))
        else:
            messages.append(("human", content))
    return messages
