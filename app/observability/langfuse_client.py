from langfuse import get_client
from langfuse.langchain import CallbackHandler

langfuse = get_client()

if not langfuse.auth_check():
    raise Exception("Langfuse authentication failed. Please check your API key.")

langfuse_handler = CallbackHandler()

def get_langfuse_handler():
    return langfuse_handler