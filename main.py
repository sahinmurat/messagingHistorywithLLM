from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

model = ChatOpenAI(model="gpt-6-luna")

agent = create_agent(
    model=model,
    tools=[],
    system_prompt="you are a helpful assistant. answer all question, if you can",
    checkpointer=InMemorySaver(),
)
store = {}
def get_session_history(session_id: str) ->BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = agent.checkpointer.load(session_id=session_id)
    return store[session_id]

thread_config = {"configurable": {"thread_id": "abc_123"}}
chain = agent | model
with_message_history = RunnableWithMessageHistory(chain, get_session_history)



if __name__ == '__main__':
    while True:
        user_input =  input(">")
        for chunk, metadata in agent.stream(
            {"messages": [{"role": "user", "content": user_input}]},
            thread_config,
            stream_mode="messages",
        ):
            if chunk.content:
                print(chunk.content, end="", flush=True)
        print()

