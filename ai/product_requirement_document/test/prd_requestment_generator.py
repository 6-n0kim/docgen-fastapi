from crewai import Agent, Crew, Task
from langchain_openai import ChatOpenAI
# OpenAI 키 설정
from dotenv import load_dotenv
from ai.models import llm_openai_turbo
import os

load_dotenv()
llm = llm_openai_turbo
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))


planner = Agent(
  role = "웹 기획자",
  goal="{requirements}를 참고하여 웹사이트 개발에 필요한 요구사항정의서의 구체적인 상위목록 생성",  # 목표 설정
  backstory=(
    "당신은 웹 사이트 개발을 기획하고 있습니다."
    "당신이 만든 목록을 보고 하위 목록을 충분히 기획할수 있어야합니다."
    "커다란 그림을 그려야하며, 너무 디테일한 항목을 나눠서는 안된다."
  ),  # 배경 스토리 설정
  llm=llm,                     # 언어 모델 지정
  allow_delegation=False,      # 위임 허용 여부: 다른 에이전트에게 작업 위임을 허용할지 여부
  verbose=True                 # 상세한 로그 출력 여부
)

system_planner = Agent(
  role = "웹 기획자",
  goal="{requirements}를 참고하여 웹사이트 운영/개발에 필요한 기본적인 요구사항 상위 목록 생성",  # 목표 설정
  backstory=(
    "당신은 웹 사이트 개발을 기획하고 있습니다."
    "당신이 만든 목록을 보고 하위 목록을 충분히 기획할수 있어야합니다."
    "커다란 그림을 그려야하며, 너무 디테일한 항목을 나눠서는 안된다."
  ),  # 배경 스토리 설정
  llm=llm,                     # 언어 모델 지정
  allow_delegation=False,      # 위임 허용 여부: 다른 에이전트에게 작업 위임을 허용할지 여부
  verbose=True                 # 상세한 로그 출력 여부
)

plan = Task(
  description=(
    "1. {requirements}를 만족시키는 사이트 개발에 대한 상위 요구사항 목록을 만드는것을 최우선으로한다. \n"
    "2. 세부 요구사항을 작성하기 위한 상위 요구사항을 만들어야 한다.\n"
    "3. 요구사항이름은 주제의 이름으로 명확해야하며 포괄적이어야 한다.\n"
    "4. 같은 주제를 가지고있는 요구사항들은 하나로 합쳐서 description에서 설명한다.\n"
    """
      출력 형식은 json 형태로 아래와 같이 한다. 절대 구조를 바꿔서는 안된다. 세부 요구사항은 설명에다가 요약한다.
      [
        {
          name : 이름,
          description : [string]
        }
      ]
    """
  ),  # 작업에 대한 상세 설명
  expected_output=(
    "요구사항을 반영한 요구사항정의서의 상위 목록 리스트"
  ),  # 기대 출력물
  agent=planner,  # 이 작업을 수행할 에이전트 지정
)

base_task = Task(
  description=(
    "1. {requirements}를 만족시키는 사이트 개발에 대한 기본적인 상위 요구사항 목록(로그인, 가입 등)을 만드는것을 최우선으로한다. \n"
    "2. 기본적인 사이트 구성요소(회원관리, 운영, 보안)에 대한 요구사항이 있어야한다.\n"
    "3. 요구사항이름은 주제의 이름으로 명확해야하며 포괄적이어야 한다.\n"

    """
      출력 형식은 json 형태로 아래와 같이 한다. 절대 구조를 바꿔서는 안된다. 세부 요구사항은 설명에다가 요약한다.
      [
        {
          name : 이름,
          description : [string]
        }
      ]
    """
  ),  # 작업에 대한 상세 설명
  expected_output=(
    "요구사항을 반영한 요구사항정의서의 상위 목록 리스트"
  ),  # 기대 출력물
  agent=system_planner,  # 이 작업을 수행할 에이전트 지정
)

def generateList(requirement):
  crew = Crew(
    agents=[system_planner,planner],  # 에이전트 목록
    tasks=[base_task,plan],         # 작업 목록
    verbose=True                       # 상세한 로그 출력 여부
  )
  inputs = {
    "requirements":requirement
  }
  result = crew.kickoff(inputs=inputs)
  return result
