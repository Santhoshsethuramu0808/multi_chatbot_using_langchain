from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage

def create_chat_chain(llm, system_prompt: SystemMessage):
    memory = ConversationBufferMemory(memory_key="history", return_messages=True)

    # Always prepend system message explicitly
    prompt = ChatPromptTemplate.from_messages([
        system_prompt,
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)
    return chain, memory
