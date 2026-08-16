import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

messages = [
    SystemMessage(
        content = "You are a Python tutor who explains concepts with simple code examples"
    ),
    HumanMessage(
        content = "Explain what a dictionary is in Python with an example"
    ),
]

model = init_chat_model(
    "groq:llama-3.3-70b-versatile",
    api_key=api_key,
)

response = model.invoke(messages)
print(response.content)