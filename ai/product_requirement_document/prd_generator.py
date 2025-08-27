import json
from pydantic import BaseModel
from typing import List

from ai.models import llm_openai_turbo, llm_openai_4o
from ai.utils import extract_json_from_response

from .agent.detail_generator import generate_details
from .agent.list_generator import generate_list
from .agent.question_generator import generate_questions
from .agent.requirement_summary import summary_requirements

llm = llm_openai_turbo
llm_4o = llm_openai_4o
class RequirementDetail(BaseModel) :
  name : str
  description : str
  def tostring(self):
    return f"세부 요구사항 이름 : {self.name}\n 세부 요구사항 설명 : {self.description}"

class Requirement(BaseModel) : 
  name : str
  description : str
  details : List[RequirementDetail]
  def tostring(self):
    return f"상위 요구사항 이름 : {self.name}\n상위 요구사항 설명 : {self.description}"+'\n'.join(detail.tostring() for detail in self.details)

class _metadata(BaseModel) :
  requirement_summary : str
class Requirement_Document(BaseModel) :
  name : str
  metadata : _metadata
  data : List[Requirement]


fixed_questions = ["어떤걸 만들건가요?", "타겟층이 어떤 사람들 인가요?"]
def generate_requirement_data(requirement_list, requirements_summary, caution = ''):
  
  data = []
  

  for requirement in requirement_list:
    name = requirement["name"]
    description = requirement["description"]
    details = generate_details(name, description,requirements_summary)
    details = extract_json_from_response(details)
    details = json.loads(details)
    
    data.append({
      "name":name,
      "description":description,
      "details": details
    })
  doc = {
    "name": "요구사항명세서",
    "metadata" : {
      "requirement_summary":requirements_summary
    },
    "data":data
  }
  # print(doc)
  doc_obj = Requirement_Document(**doc)
  return doc_obj


def generate_document():
  # questions = fixed_questions
  # question_answer_list = []
  # for question in questions:
  #   answer = input(question)
  #   question_answer_list.append(f"{question} : {answer}")
  # gen_questions = generate_questions(question_answer_list)
  # gen_questions = extract_json_from_response(gen_questions)
  # print(gen_questions)
  # gen_questions = json.loads(gen_questions)
  # gen_questions = gen_questions['questions']
  # for question in gen_questions:
  #   answer = input(question)
  #   question_answer_list.append(f"{question} : {answer}")
  # summary = summary_requirements(question_answer_list)
  # print(summary)
  summary = """
사용자가 어떻게 입력을 하고, 결과를 어떻게 확인할 수 있는지 구체적으로 설명해 주실 수 있나요?현재위치 찾는위치, 경로
사이트에 어떤 기능이 포함되어야 하며, 어떤 정보를 제공해야 할까요?길찾기와 가는 경로 및 소요시간
사용자 경험을 개선하기 위해 특별히 고려해야 할 사항은 무엇인가요?보기편하게
모바일 환경에서도 사용할 수 있도록 고려해야 할 사항이 있을까요?헷갈리지 않게
길찾기 사이트를 만들어 일반인을 대상으로 현재 위치와 찾는 위치를 입력하여 경로와 소요시간을 확인할 수 있도록 해야 합니다. 사용자 경험을 개선하기 위해 보기 편한 인터
페이스를 고려하고, 모바일 환경에서도 헷갈리지 않게 사용할 수 있도록 고려해야 합니다.
"""
  require_list = generate_list(summary)
  require_list = extract_json_from_response(require_list)
  require_list = json.loads(require_list)
  require_data = generate_requirement_data(require_list,summary)
  return require_data

if __name__ == "__main__":
  generate_document()
  
  