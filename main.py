from langchain_core.messages import HumanMessage
from agent import build_graph
from retriever.dataloaer import docs
from retriever.retriever import initialize_retriever
def main():
    initialize_retriever(docs)
    agent = build_graph()
    messages = [
        HumanMessage(
            content="Tell me about our guest named 'Lady Ada Lovelace'"
        )
    ]

    response = agent.invoke({"messages": messages})

    print("Alfred's Response:")
    print(response["messages"][-1].content)

if __name__ == "__main__":
    main()
