from ai.product_requirement_document.prd_generator import Requirement_Document
from pydantic import BaseModel, Field
from typing import Optional, List

class ProductRequirementsDocumentRequest(BaseModel):
  owner_id : str
  project_id : str
  requirement : str

class ProductRequirementsDocument(BaseModel):
  owner_id : str
  project_id : str
  status : str = Field(...,examples="finish")
  document : Requirement_Document = None