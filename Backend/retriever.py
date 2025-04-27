import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone as LangPinecone

# Initialize Pinecone
pinecone.init(
    api_key="pcsk_2PtCE2_FGAixBLUzs6w9VbHPUXNVhh2WpQaeYDZ7KkVyBuvEyP7KN1QTcXwBXUFBpszX6b",
    environment="us-west1-gcp"
)
index_name = "adaptive-tutor-index"
index = pinecone.Index(index_name)

embeddings = OpenAIEmbeddings()
vectorstore = LangPinecone(index, embeddings.embed_query, "text")
retriever = vectorstore.as_retriever()

def retrieve_context(query: str) -> str:
    """Retrieve relevant context from Pinecone; fallback if no results."""
    docs = retriever.get_relevant_documents(query)
    if not docs:
        return "No relevant documents found. Proceed based on general knowledge."
    context = "\n".join([doc.page_content for doc in docs[:3]])
    return context