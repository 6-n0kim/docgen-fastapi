from pydantic import BaseModel
from typing import List, Optional

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


class FunctionalSpecificationDetail(BaseModel):
  name : str
  description : str
  def tostring(self):
    return f"세부 기능 이름 : {self.name}\n 세부 기능 설명 : {self.description}"
class FunctionalSpecificationFunctional(BaseModel):
  name : str
  description : str
  details: List[FunctionalSpecificationDetail]
  def tostring(self):
    return f"상위 기능 이름 : {self.name}\n상위 기능 설명 : {self.description}"+'\n'.join(detail.tostring() for detail in self.details)
class FunctionalSpecification(BaseModel):
  name : str
  metadata : str
  data : List[FunctionalSpecificationFunctional]


class ServicePolicyRole(BaseModel):
  name: Optional[str] = None
  description: Optional[str] = None
  def tostring(self):
    return f"{self.name} : {self.description}"

class ServicePolicyDetail(BaseModel):
  role : Optional[str] = None
  create: Optional[str] = None
  read: Optional[str] = None
  update: Optional[str] = None
  delete: Optional[str]  = None
  description : Optional[str]  = None

class ServicePolicyItem(BaseModel):
  name : Optional[str] = None
  description : Optional[str] = None
  functional_id: Optional[str] = None
  roles: List[ServicePolicyDetail] = None

class ServicePolicy(BaseModel):
  name : str = None
  metadata : str = None
  data : List[ServicePolicyItem] = None