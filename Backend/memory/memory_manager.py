from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.memory import ConversationBufferMemory  # Update to latest import

def memory(tag: str):
    chat_history = InMemoryChatMessageHistory()
    return ConversationBufferMemory(
        chat_memory=chat_history,
        return_messages=True,
        memory_key=f"chat_history_{tag}"
    )

