from click import command
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI(model="gpt-6-luna")


if __name__ == '__main__':
    message = [
        HumanMessage(content="Hey, my name is donald trump, the president of the usa"),
        AIMessage(content="Nice to meet you, sir"),
        HumanMessage(content="Hey, what is my name")

    ]
    response = model.invoke(message)
    print(response.content)

