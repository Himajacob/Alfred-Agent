from langchain_core.messages import HumanMessage, AIMessage
from agent import build_graph
from retriever.dataloaer import docs
from retriever.retriever import initialize_retriever
import gradio as gr
from observability.langfuse_client import get_langfuse_handler


initialize_retriever(docs)
agent = build_graph()
handler = get_langfuse_handler()

def chat(message, history):
    messages = []

    for msg in history:
        if msg['role'] == 'user':
            messages.append(HumanMessage(content=msg['content']))
        elif msg['role'] == 'assistant':
            messages.append(AIMessage(content=msg['content']))

    messages.append(HumanMessage(content=message))
    response = agent.invoke({"messages": messages},
                            config={"callbacks":[handler]})


    reply = response["messages"][-1].content
    return reply

gr.ChatInterface(
    fn=chat,
    title="🦇 Alfred - Wayne Manor Assistant",
    description="Ask Alfred about guests, news, weather, or anything else."
).launch(server_name="0.0.0.0", server_port=7860)