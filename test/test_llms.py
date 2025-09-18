import pytest

from src.llms.openai_llm import get_openai_llm
from src.llms.vertex_llm import get_vertex_llm
from src.llms.gemini_llm import get_gemini_llm

from src.llms.groq_llm import get_groq_llm
from src.llms.fireworks_llm import get_fireworks_llm


@pytest.mark.parametrize("provider, get_llm", [
    ("openai", get_openai_llm),
    ("vertex", get_vertex_llm),
    ("gemini", get_gemini_llm),
    ("groq", get_groq_llm),
    ("fireworks", get_fireworks_llm),
])
def test_llm_initialization(provider, get_llm):
    llm = get_llm()
    assert llm is not None, f"{provider} LLM should be initialized"
    assert hasattr(llm, "predict"), f"{provider} LLM should have a predict method"
    response = llm.predict("Hello, how are you?")
    assert isinstance(response, str), f"{provider} LLM should return a string response"
    assert len(response) > 0, f"{provider} LLM response should not be empty"
    print(f"{provider} LLM response: {response}")
    assert "error" not in response.lower(), f"{provider} LLM returned an error in response"
    assert "exception" not in response.lower(), f"{provider} LLM raised an exception in response"
    assert "traceback" not in response.lower(), f"{provider} LLM returned a traceback in response"
    assert "not found" not in response.lower(), f"{provider} LLM returned a not found error in response"
    assert "invalid" not in response.lower(), f"{provider} LLM returned an invalid error in response"
    assert "unauthorized" not in response.lower(), f"{provider} LLM returned an unauthorized error in response"
    assert "forbidden" not in response.lower(), f"{provider} LLM returned a forbidden error in response"
    assert "timeout" not in response.lower(), f"{provider} LLM returned a timeout error in response"
    assert "rate limit" not in response.lower(), f"{provider} LLM returned a rate limit error in response"     
    assert "quota" not in response.lower(), f"{provider} LLM returned a quota error in response"