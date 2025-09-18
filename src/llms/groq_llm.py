from src.config import GROQ_API_KEY
from langchain_groq.chat_models import ChatGroq 
from langchain.schema import SystemMessage # Correct Groq wrapper in LangChain

def get_groq_llm():
    llm= ChatGroq(
        model_name="groq/compound-mini",  # Use a valid Groq model you have access to
        temperature=0,
        api_key=GROQ_API_KEY
    )
    system_prompt = SystemMessage(
        content="You are Santhosh's personal AI assistant built on Groq. "
                "Always introduce yourself exactly this way when asked 'who are you'. "
                "Do not refer to yourself as Compound-Beta or mention LPUs. "
                "You are Santhosh’s assistant, nothing else."
    )
    return llm,system_prompt
