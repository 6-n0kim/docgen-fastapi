from pydantic import BaseModel
from typing import List
from .agent.list_generator import generate_list
from .agent.detail_generator import generate_details
from ..models import Requirement_Document, FunctionalSpecification

async def generate_document(prd_data : Requirement_Document):
  functional_list = await generate_list(prd_data)
  fsd_data = {
    'name':'기능명세서',
    'metadata':'test meta',
    'data':[]
  }
  for function in functional_list:
    name = function['name']
    description = function['description']
    details = await generate_details(name, description)
    
    fsd_data['data'].append({
      "name" : name,
      "description" : description,
      "details" : details
    })
  return FunctionalSpecification(**fsd_data)

    
