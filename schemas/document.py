from ai.product_requirement_document.prd_generator import Requirement_Document
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, timezone

class ProductRequirementsDocumentRequest(BaseModel):
  owner_id : str
  project_id : str
  requirement : str

class ProductRequirementsDocument(BaseModel):
  owner_id : str= Field(...,example="owner_user_id")
  project_id : str = Field(...,example="project_id")
  status : str = Field(...,example="finish")
  create_date : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
  document : Requirement_Document = None

class ProductRequirementsDocumentListItemResponse(BaseModel):
  id : str= Field(...,example="id")
  owner_id : str= Field(...,example="owner_user_id")
  project_id : str = Field(...,example="project_id")
  status : str = Field(...,example="finish")
  create_date : datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class DocumentIdResponse(BaseModel):
  document_id : str

class DocumentQuestions(BaseModel):
  questions : List[str]