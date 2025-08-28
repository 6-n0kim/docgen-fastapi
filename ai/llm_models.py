import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


llm_openai_turbo = ChatOpenAI(
  model_name="gpt-3.5-turbo",
  temperature=0.7,
  api_key=os.getenv("OPENAI_API_KEY")
)

llm_openai_4o = ChatOpenAI(
  model_name="gpt-4o",
  temperature=0.7,
  api_key=os.getenv("OPENAI_API_KEY"),
  max_tokens=4096
)