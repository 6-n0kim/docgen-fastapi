from pydantic import BaseModel
from typing import List
from .agent.list_generator import generate_list
from .agent.detail_generator import generate_details
from ..product_requirement_document.prd_generator import Requirement_Document

class _detail(BaseModel):
  name : str
  description : str

class _functional(BaseModel):
  name : str
  description : str
  details: List[_detail]

class FunctionalSpecification(BaseModel):
  name : str
  metadata : str
  data : List[_functional]

def generate_document(prd_data : Requirement_Document):
  functional_list = generate_list(prd_data)
  fsd_data = {
    'name':'기능명세서',
    'metadata':'test meta',
    'data':[]
  }
  for function in functional_list:
    name = function['name']
    description = function['description']
    print(f"name : {name}")
    print(f"description : {description}")
    details = generate_details(name, description)
    
    fsd_data['data'].append({
      "name" : name,
      "description" : description,
      "details" : details
    })
  return FunctionalSpecification(**fsd_data)

    
