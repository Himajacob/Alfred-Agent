from langchain_ollama import ChatOllama

def get_llm():
    return ChatOllama(
        model="llama3.1:8b",
        temperature=0.7,
    )
#model="llama3.2:3b",
#mistral:7b