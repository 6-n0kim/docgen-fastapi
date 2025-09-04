from ai.llm_models import llm_openai_turbo, llm_claude_3_7
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = llm_claude_3_7

async def generate_details(requirement_name, requirement_description, requirement_summary, caution = ''):
  """디테일 생성"""
  template = """
    당신은 웹 개발 기획자 입니다.
    주어진 상위 요구사항에 포함된 하위 요구사항목록을 작성하시오.
    누락된 요구가 없도록 생성하고 설명을 자세히 작성하시오.
    정해진 json형태로만 만들어주고 다른 설명은 절대 추가하지 마세요.
    {caution}

    답변 형태는 정해진 json 형태로만 만들어주고 다른 설명은 절대 추가하지 마세요.
    ```json
    {json_template}
    ```
    요구사항
    요구 사항 이름 : {name}
    요구 사항 설명 : {description}
  """
  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm | StrOutputParser()
  return await chain.ainvoke({
    "caution":caution,
    "json_template": """
    [{
      "name":상세 요구사항 이름,
      "description" : 상세 요구사항 설명
    }]
    """,
    "name":requirement_name,
    "description":requirement_description
  })