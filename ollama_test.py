from langchain_community.chat_models import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

chat_model = ChatOllama(
    model="ryota39-Phi-3-mini-4k-instruct-dpo-Q4_0.gguf",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

# 従来のLangchain
from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="あなたは優秀なアシスタントです。英語で考え日本語で必ず回答します。"),
    HumanMessage(content="AIの歴史を詳細に解説してください。")
    ]

chat_model.invoke(messages)

# LCEL
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "あなたは優秀なアシスタントです。英語で考え日本語で必ず回答します。"),
        ("human", "{question}"),
    ]
)

chain = prompt | chat_model
chain.invoke({"question": prompt})