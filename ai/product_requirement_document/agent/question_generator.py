from ai.llm_models import llm_openai_turbo, llm_claude_3
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = llm_claude_3

async def generate_questions(questions_answers_list, caution=''):
  """질문 생성 함수"""
  template = """
    당신은 웹 개발 기획자 입니다.
    질문 내역을 보고 좋은 요구사항 정의서를 작성하기 위한 추가 질문 목록을 작성해 주세요.
    {caution}
    번호는 제외하고,
    답변 형태는 정해진 json 형태로만 만들어주고 다른 설명은 절대 추가하지 마세요.
    ```json
    {json_template}
    ```
    질의응답 내용
    {questions_answers_list}
  """
  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm | StrOutputParser()
  result = await chain.ainvoke({
    "caution":caution,
    "questions_answers_list":'\n'.join(questions_answers_list),
    "json_template": '{"questions":[string]}'
  })
  return result