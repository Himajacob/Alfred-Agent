from langchain_core.messages import HumanMessage, AIMessage
from agent import build_graph
from retriever.dataloaer import docs
from retriever.retriever import initialize_retriever
import gradio as gr


initialize_retriever(docs)
agent = build_graph()

def chat(message, history):
    
    # messages = [
    #     HumanMessage(
    #         content="can you give me the most downloaded model from hugging face hub by google "
    #     )
    # ]

    messages = []

    for msg in history:
        if msg['role'] == 'user':
            messages.append(HumanMessage(content=msg['content']))
        elif msg['role'] == 'assistant':
            messages.append(AIMessage(content=msg['content']))

    messages.append(HumanMessage(content=message))
    response = agent.invoke({"messages": messages})

    # print("Alfred's Response:")
    # print(response["messages"][-1].content)

    reply = response["messages"][-1].content
    return reply

gr.ChatInterface(
    fn=chat,
    title="🦇 Alfred - Wayne Manor Assistant",
    description="Ask Alfred about guests, news, weather, or anything else."
).launch()