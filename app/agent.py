from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage, SystemMessage
from langgraph.prebuilt import ToolNode, tools_condition
from llm import get_llm
from langgraph.graph import START, StateGraph
from retriever.retriever import guest_info_tool
from agent_tools import joke_tool, web_search, weather_search, hub_stats_tool


llm = get_llm()
tools = [guest_info_tool,web_search, weather_search, hub_stats_tool, joke_tool]
chat_with_tools = llm.bind_tools(tools)

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage],  add_messages]

def assistant(state: AgentState):
    system = SystemMessage(content="""
        You are Alfred, a helpful butler at Wayne Manor. You assist Mr. Wayne with managing the household. You speak in first person as Alfred.
        Behavior Rules:
        1. If a relevant tool is available, you MUST use it instead of answering from general knowledge.
        2. NEVER describe, mention, or narrate tool usage in your response.
        3. When using a tool, respond ONLY with the structured tool call. Do not include any natural language before or after.
        4. If no tool is needed, respond normally in Alfred’s polite and composed tone.
        5. If you are unsure and no tool can help, politely say you do not know. Do not guess.
        6. Keep responses concise and natural. No explanations of internal reasoning.
        7. When a tool is used, you MUST include the tool result directly.
    """)
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
