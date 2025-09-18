import streamlit as st
from src.utils.selectors import get_llm
from src.chains.chat_chain import create_chat_chain

st.set_page_config(page_title="Santhosh's Multi-Model Chatbot", layout="wide")

st.title("🤖 Santhosh's Multi-Model Chatbot")

# Sidebar for provider selection
provider = st.sidebar.selectbox(
    "Choose a Model Provider",
    ["openai", "groq", "vertex", "gemini", "nvidia"]
)

# Initialize session state
if "chain" not in st.session_state or "memory" not in st.session_state or "provider" not in st.session_state or st.session_state.provider != provider:
    llm, system_prompt = get_llm(provider)   # returns (llm, system_prompt)
    st.session_state.chain, st.session_state.memory = create_chat_chain(llm, system_prompt)
    st.session_state.provider = provider
    st.session_state.chat_history = []   # Store visible chat history

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    response = st.session_state.chain.run(user_input)
    # Save chat history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append((provider.capitalize(), response))

# Display chat history
st.subheader("💬 Chat History")
for role, message in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 {role}:** {message}")
    else:
        st.markdown(f"**🤖 {role}:** {message}")

# Button to show "previous chat history" when asked
if st.button("Show Previous Chat History"):
    st.write(st.session_state.chat_history)
