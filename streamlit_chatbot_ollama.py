import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_models import ChatOllama
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.callbacks.base import BaseCallbackHandler

# callback
class StreamHandler(BaseCallbackHandler):
    
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs):
        self.text += token
        self.container.markdown(self.text)

# history
msgs = StreamlitChatMessageHistory(key="history")

# prompt
from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "あなたは優秀なアシスタントです。英語で考え、日本語で回答します。"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

# Ollamaを初期化
llm = ChatOllama(
    model="ryota39-Phi-3-mini-4k-instruct-dpo-Q4_0.gguf",
)

# StreamlitアプリケーションのUI
st.title("💬 Chatbot")
st.caption("A streamlit chatbot")

# Chain
chain = prompt | llm

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: msgs,  # Always return the instance created earlier
    input_messages_key="question",
    history_messages_key="history",
)

for msg in msgs.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input():

    st.chat_message("human").write(prompt)

    with st.chat_message("ai"):

        container = st.empty()
        st_callback = StreamHandler(container)
        # sessin_id and callbacks
        config = {"configurable": {"session_id": "any"},
                "callbacks": [st_callback]
                }
        # generate response.
        response = chain_with_history.invoke({"question": prompt}, config)
        container.write(response.content)

