from ai.models import llm_openai_turbo
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = llm_openai_turbo

def summary_requirements(question_answer_list,caution=''):
  """질의응답 요약 함수"""
  template = """
    당신은 웹 개발 기획자 입니다.
    주어진 질의응답을 핵심을 포함하여 요약하세요.
    해당 요약만으로 요구사항명세서를 충분히 만들수 있어야 합니다.
    {caution}

    질의응답 내용
    {question_answer_list}
  """
  prompt = PromptTemplate.from_template(template)
  chain = prompt | llm | StrOutputParser()
  return chain.invoke({
    "caution":caution,
    "question_answer_list":'\n'.join(question_answer_list)
  })