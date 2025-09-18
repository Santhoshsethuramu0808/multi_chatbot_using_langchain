from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import GOOGLE_API_KEY
from langchain.schema import SystemMessage

def get_vertex_llm():
    """
    Returns a Vertex LLM instance + a system prompt.
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # latest Vertex model
        temperature=0,
        api_key=GOOGLE_API_KEY
    )

    system_prompt = SystemMessage(
        content="You are Santhosh's personal AI assistant built on Groq. "
                "Always introduce yourself exactly this way when asked 'who are you'. "
                "Do not refer to yourself as Compound-Beta or mention LPUs. "
                "You are Santhosh’s assistant, nothing else."
    )

    return llm,system_prompt
