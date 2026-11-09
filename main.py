from click import command
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

model = ChatOpenAI(model="gpt-6-luna")

store = {}

def get_session_history(session_id:str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

prompt =  ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. answer all question, if you can"),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | model
config = {"configurable": {"session_id":"abc_123"}}
with_message_history = RunnableWithMessageHistory(chain, get_session_history)



if __name__ == '__main__':
    user_input =  input(">")
    response =  with_message_history.invoke(
        [
            HumanMessage(content=user_input),
        ],
        config=config
    )

