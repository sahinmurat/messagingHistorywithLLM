from click import command
from dotenv import load_dotenv
from langchain.agents import create_agent
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

thread_config = {"configurable": {"thread_id": "abc_123"}}



if __name__ == '__main__':
    while True:
        user_input =  input(">")
        response = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]},
            thread_config,
        )["messages"][-1].content
        print(response)

