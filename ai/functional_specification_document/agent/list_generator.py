import json
from ai.models import llm_openai_turbo
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ...product_requirement_document.prd_generator import Requirement, Requirement_Document
from ai.utils import extract_json_from_response

llm = llm_openai_turbo

def generate_functional_list(requirement_item : Requirement, caution = ''):
  """질문 생성 함수"""
  template = """
    당신은 웹 개발 기획자 입니다.
    주어진 요구사항들을 읽고 기능정의서에
    필요한 기능 목록을 작성하시오. 큰 개념의 기능 목록으로 나누고
    세부 기능에 대한 내용은 description에 작성하시오
    {caution}

    답변 형태는 정해진 json 형태로만 만들어주고 다른 설명은 절대 추가하지 마세요.
    ```json
    {json_template}
    ```
    요구사항 정보
    {requirement_item}
  """
  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm | StrOutputParser()
  return chain.invoke({
    "caution":caution,
    "requirement_item":requirement_item.tostring(),
    "json_template": """
    [{
      "name":기능 이름,
      "description" : 기능 설명
    }]
"""
  })

def generate_list(requirement_document : Requirement_Document):
  functional_list = []
  for requirement in requirement_document.data:
    result = generate_functional_list(requirement)
    result = extract_json_from_response(result)
    functional_list.extend(json.loads(result))
  return functional_list