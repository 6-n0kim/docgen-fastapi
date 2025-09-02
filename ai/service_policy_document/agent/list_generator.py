import json
from ai.llm_models import llm_openai_turbo
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ...models import FunctionalSpecificationFunctional, FunctionalSpecification, ServicePolicyItem
from ai.utils import extract_json_from_response
from typing import List

llm = llm_openai_turbo

async def generate_policy_list(functional_item : FunctionalSpecificationFunctional, caution = ''):
  """질문 생성 함수"""
  template = """
    당신은 웹 개발 기획자 입니다.
    기능정의서를 보고 정책 정의서를 작성할 겁니다.
    주어진 기능들에 필요한 정책들을 만들어주세요.
    주어진 기능들마다 정책 하나씩 있어야 합니다.
    {caution}

    답변 형태는 정해진 json 형태로만 만들어주고 다른 설명은 절대 추가하지 마세요.
    ```json
    {json_template}
    ```
    기능 정보
    {functional_item}
  """
  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm | StrOutputParser()
  return await chain.ainvoke({
    "caution":caution,
    "functional_item":functional_item.tostring(),
    "json_template": """
    [
      {
        "id":string,
        "name":string,
        "description" : string
      }
    ]
"""
  })

async def generate_list(functional_document : FunctionalSpecification)->List[ServicePolicyItem]:
  policy_list = []
  for requirement in functional_document.data:
    result = await generate_policy_list(requirement)
    result = extract_json_from_response(result)
    result = json.loads(result)
    for item in result:
      for _ in range(5):
        try:
          _new = ServicePolicyItem()
          _new.name = item["name"]
          _new.description = item["description"]
          _new.roles = []
          policy_list.append(_new)
          break
        except:
          print("error check")
    # policy_list.extend(json.loads(result))
  return policy_list