from pydantic import BaseModel, Field
from typing import Optional, List

class TestModel(BaseModel):
  test_name: str = Field(..., examples="test_names")
  description: str = Field(..., examples="test_description")

class TestModelInDB(TestModel):
  id : str






class ProductRequirementsDocumentDetail(BaseModel):
  name: str = Field(..., examples='prd detail name')
  description : str = Field(..., examples='prd detail description')

class ProductRequirementsDocumentData(BaseModel):
  id: str = Field(..., examples="ID-1")
  system: str = Field(..., examples="BackOffice")
  name: str = Field(...,examples="requirement")
  details: List[ProductRequirementsDocumentDetail] = Field(default_factory=list)

class ProductRequirementsDocument(BaseModel):
  id: str = Field(..., examples="unique_id")
  data: List[ProductRequirementsDocumentData] = Field(default_factory=list)