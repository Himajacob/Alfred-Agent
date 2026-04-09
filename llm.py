from langchain_ollama import ChatOllama

def get_llm():
    return ChatOllama(
        model="llama3.2:3b",
        temperature=0.7,
        base_url="http://host.docker.internal:11434",
    )
#model="llama3.2:3b",
#mistral:7b
#model="llama3.1:8b"