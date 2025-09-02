import json
from ai.llm_models import llm_openai_turbo
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ...models import ServicePolicyRole
from ai.utils import extract_json_from_response
from typing import List

llm = llm_openai_turbo

async def _generate_role_list(requirement : str, caution = '') -> List[ServicePolicyRole]: 
  """질문 생성 함수"""
  template = """
    당신은 웹 개발 기획자 입니다.
    주어진 요구사항들을 읽고 정책정의서에 필요한 사용자 역할 목록을 생성하시오.
    {caution}

    답변 형태는 정해진 json 형태로만 만들어주고 다른 설명은 절대 추가하지 마세요.
    ```json
    {json_template}
    ```
    요구사항 정보
    {requirement}
  """
  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm | StrOutputParser()
  result = await chain.ainvoke({
    "caution":caution,
    "requirement": requirement,
    "json_template": """
    [{
      "name":역할 이름,
      "description" : 역할 설명
    }]
    """
    })
  result = extract_json_from_response(result)
  roles = json.loads(result)
  return [ServicePolicyRole(**role) for role in roles]


async def generate_role_list(requirement : str) -> List[ServicePolicyRole]:
  roles = await _generate_role_list(requirement)
  return roles