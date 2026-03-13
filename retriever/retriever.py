from langchain_community.retrievers import BM25Retriever
from langchain_core.tools import Tool

bm25_retriever = None
def initialize_retriever(docs):
    global bm25_retriever
    if bm25_retriever is None:
        bm25_retriever = BM25Retriever.from_documents(docs)

def extract_text(query: str)->str:
    """Retrieves detailed information about gala guests based on their name or relation."""
    results = bm25_retriever.invoke(query)
    if results:
        return "\n\n".join([doc.page_content for doc in results[:3]])
    else:
        return "No relevant information found about the guest."

guest_info_tool = Tool(
    name="guest_info_retriever",
    func=extract_text,
    description="Retrieves detailed information about gala guests based on their name or relation."
)
