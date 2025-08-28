from ai.llm_models import llm_openai_turbo
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ai.utils import extract_json_from_response
import json
llm = llm_openai_turbo

def generate_details(functional_name, functional_description, caution = ''):
  """디테일 생성"""
  template = """
    당신은 웹 개발 기획자 입니다.
    기능 정의서를 만드는데 필요한 상세 기능들을 작성할겁니다.
    주어진 기능에 포함된 상세 기능들을 작성하시오.
    누락된 기능 없도록 생성.
    {caution}

    답변 형태는 정해진 json 형태로만 만들어주고 다른 설명은 절대 추가하지 마세요.
    ```json
    {json_template}
    ```
    요구기능
    요구 기능 이름 : {name}
    요구 기능 설명 : {description}
  """
  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm | StrOutputParser()
  result = chain.invoke({
    "caution":caution,
    "json_template": """
    [{
      "name":상세 기능 이름,
      "description" : 상세 기능 설명
    }]
    """,
    "name":functional_name,
    "description":functional_description
  })
  return json.loads(extract_json_from_response(result)) 