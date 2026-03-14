from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_core.tools import tool
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


