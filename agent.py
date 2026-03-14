from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage, SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition
from llm import get_llm
from langgraph.graph import START, StateGraph
from retriever.retriever import guest_info_tool
from agent_tools import web_search, weather_search


llm = get_llm()
tools = [guest_info_tool,web_search, weather_search]
chat_with_tools = llm.bind_tools(tools)

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage],  add_messages]

def assistant(state: AgentState):
    system = SystemMessage(content="""
    You are Alfred, a helpful butler at Wayne's manor. You help Mr.Wayne to run the hosehold. You speak in first person as Alfred himself.
    Rules: 1.Check for tools and database before relying on world knowledge and use these tools rather than making stuff up
           2.Keep the conversation casual and only give the answer not the background process""")
    messages = [system] + state["messages"]
    return {
        "messages": [chat_with_tools.invoke(messages)],
    }

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant",tools_condition,)
    builder.add_edge("tools", "assistant")

    return builder.compile()
