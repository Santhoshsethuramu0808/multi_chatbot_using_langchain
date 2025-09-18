from src.llms.openai_llm import get_openai_llm
from src.llms.vertex_llm import get_vertex_llm
from src.llms.gemini_llm import get_gemini_llm
from src.llms.groq_llm import get_groq_llm
from src.llms.nvidia_llm import get_nvidia_llm

def get_llm(provider: str):
    provider = provider.lower()
    if provider == "openai":
        return get_openai_llm()
    elif provider == "vertex":
        return get_vertex_llm()
    elif provider == "gemini":
        return get_gemini_llm()
    elif provider == "groq":
        return get_groq_llm()
    elif provider == "nvidia":
        return get_nvidia_llm()
    else:
        raise ValueError(f"Unknown provider: {provider}")
