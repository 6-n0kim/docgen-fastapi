import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# OPEN_AI
# 모델 정보
# https://platform.openai.com/docs/models
# https://platform.openai.com/docs/pricing

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

# GEMINI
# 모델 정보 https://ai.google.dev/gemini-api/docs/models?hl=ko

llm_gemini_2_0_flash_lite = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    temperature=0.7,
    max_output_tokens=8192,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

llm_gemini_2_5_flash = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    max_output_tokens=8192,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

llm_gemini_2_5_flash_lite = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7,
    max_output_tokens=8192,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

# CLAUDE
# 모델 정보 https://docs.anthropic.com/ko/docs/about-claude/models/overview

llm_claude_3 = ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0.7,
    max_tokens=200, 
    api_key=os.getenv("CLAUDE_API_KEY"),
)