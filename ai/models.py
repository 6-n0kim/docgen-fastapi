from pydantic import BaseModel
from typing import List

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

class Requirement_Metadata(BaseModel) :
  requirement_summary : str
class Requirement_Document(BaseModel) :
  name : str
  metadata : Requirement_Metadata
  data : List[Requirement]