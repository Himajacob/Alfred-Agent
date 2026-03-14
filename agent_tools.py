from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_core.tools import tool, Tool
from huggingface_hub import list_models
from dotenv import load_dotenv
import os

load_dotenv()

web_search = DuckDuckGoSearchRun(
    name="web_search",
    description= "Search the internet for latest news, current events, and real-time information."
)

@tool 
def weather_search(location: str) -> str:
     """Get current weather information for a specific location given the city name"""
     weather = OpenWeatherMapAPIWrapper()
     return weather.run(location)

def get_hub_stats(author: str) -> str:
    """Fetches the most downloaded model from a specific author on the Hugging Face Hub."""
    try:
        models = list(list_models(author=author, sort="downloads", direction=-1, limit=1))
        if models:
            model = models[0]
            return f"The most downloaded model by {author} is '{model.modelId}' with {model.downloads} downloads."
        else:
            return f"No models found for author '{author}'."
    except Exception as e:
        return f"An error occurred while fetching models for author '{author}': {str(e)}"

hub_stats_tool = Tool(
    name="get_hub_stats",
    func=get_hub_stats,
    description="Fetches the most downloaded model from a specific author on the Hugging Face Hub."
)    


