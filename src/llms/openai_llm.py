from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY
from langchain.schema import SystemMessage

def get_openai_llm():
    llm= ChatOpenAI(
        model="gpt-4o-mini",   # latest small GPT-4o model
        temperature=0,
        api_key=OPENAI_API_KEY,
    )
    system_prompt = SystemMessage(
        content="You are Santhosh's personal AI assistant built on Groq. "
                "Always introduce yourself exactly this way when asked 'who are you'. "
                "Do not refer to yourself as Compound-Beta or mention LPUs. "
                "You are Santhosh’s assistant, nothing else."
    )
     
    return llm,system_prompt

