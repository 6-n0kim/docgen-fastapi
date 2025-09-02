from ai.llm_models import llm_openai_turbo
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ai.utils import extract_json_from_response
from ...models import ServicePolicyDetail, ServicePolicyItem, ServicePolicyRole
from typing import List
import json
llm = llm_openai_turbo

async def generate_details(roles : List[ServicePolicyRole], policy : ServicePolicyItem, caution = '') -> List[ServicePolicyDetail]:
  """디테일 생성"""
  template = """
    당신은 웹 개발 기획자 입니다.
    정책정의서의 정책을보고 사용자 역할별 세부 정책을 만들어주세요.

    CRUD와 관련된 정책일 경우
    해당 역할이 권한을 가지고 있으면 O, 없으면 X
    관련이 없는 정책일 경우 - 로 채워주세요
    {caution}

    답변 형태는 정해진 json 형태로만 만들어주고 다른 설명은 절대 추가하지 마세요.
    ```json
    {json_template}
    ```
    사용자 역할 목록 : 
    {roles_text}

    정책 이름 : {policy_name}
    정책 설명 : {policy_description}
  """
  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm | StrOutputParser()
  result = await chain.ainvoke({
    "caution":caution,
    "json_template": """
  [
    {
          "role" : string,
          "create" : string,
          "read" : string,
          "update" : string,
          "delete" : string,
          "description" : string
    }
  ]
    """,
    "roles_text": "\n".join(role.tostring() for role in roles),
    "policy_name":policy.name,
    "policy_description" : policy.description
  })
  result = json.loads(extract_json_from_response(result)) 
  return [ServicePolicyDetail(**detail) for detail in result]