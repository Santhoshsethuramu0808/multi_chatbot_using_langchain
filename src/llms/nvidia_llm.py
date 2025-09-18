from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from src.config import NVIDIA_API_KEY
from langchain.schema import SystemMessage  # Add your NVIDIA API key here

def get_nvidia_llm():
    """
    Returns a ChatNVIDIA LLM instance wrapped in a LangChain pipeline.
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI assistant named Fred."),
            ("user", "{input}")
        ]
    )
    
    # Chain: prompt -> NVIDIA LLM -> string output
    chain = prompt | ChatNVIDIA(
        model="meta/llama3-8b-instruct",
        api_key=NVIDIA_API_KEY
    ) | StrOutputParser()
    
    system_prompt = SystemMessage(
        content="You are Santhosh's personal AI assistant built on Groq. "
                "Always introduce yourself exactly this way when asked 'who are you'. "
                "Do not refer to yourself as Compound-Beta or mention LPUs. "
                "You are Santhosh’s assistant, nothing else."
    )
    return chain,system_prompt