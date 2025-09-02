from pydantic import BaseModel
from typing import List
from .agent.list_generator import generate_list
from .agent.detail_generator import generate_details
from .agent.role_generator import generate_role_list
from ..models import FunctionalSpecification, ServicePolicy

async def generate_document(requirement: str, fsd_data : FunctionalSpecification)->ServicePolicy:
  service_policy = ServicePolicy()
  service_policy.name = "정책정의서"
  service_policy.metadata = "test meta"
  policy_list = await generate_list(fsd_data)
  fsd_data = {
    'name':'기능명세서',
    'metadata':'test meta',
    'data':[]
  }
  roles = await generate_role_list(requirement)
  for policy in policy_list:
    for _ in range(5):
      try:
        name = policy.name
        description = policy.description
        details = await generate_details(roles, policy)
        policy.roles = details
        break
      except:
        print("error_details")
  
  service_policy.data = policy_list
  return service_policy

    
