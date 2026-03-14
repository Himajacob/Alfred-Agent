from langchain_community.tools import DuckDuckGoSearchRun

web_search = DuckDuckGoSearchRun(
    name="web_search",
    description= "Search the internet for latest news, current events, and real-time information."
)
