from ai.llm_models import llm_openai_4o
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = llm_openai_4o

async def generate_list(summary_requirement, caution = ''):
  """목록 생성 함수"""
  template = """
    당신은 웹 개발 기획자 입니다.
    주어진 내용을 읽고, 필요한 요구사항들의 카테고리의 이름과 설명을 작성하세요.
    요구사항 외에 사이트를 만드는데 필요한 기본 기능도 고려하고,
    사이트를 만드는데 필요한 가장 상위의 카테고리(회원관리, 관리자페이지 등)들을 최대한 전부 작성하되 큰 개념으로 나누고,
    세부 요구사항은 설명으로 작성하세요.
    {caution}

    답변 형태는 정해진 json 형태로만 만들어주고 다른 설명은 절대 추가하지 마세요.
    ```json
    {json_template}
    ```
    요구사항
    {summary_requirement}
  """
  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm | StrOutputParser()
  return await chain.ainvoke({
    "caution":caution,
    "summary_requirement":summary_requirement,
    "json_template": """
    [{
      "name":요구사항 이름,
      "description" : 요구사항 설명
    }]
"""
  })