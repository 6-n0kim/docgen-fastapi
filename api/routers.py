from fastapi import APIRouter
from .endpoints import requirement_document,functional_document,project

api_router = APIRouter()
api_router.include_router(
  requirement_document.router, 
  prefix="/document/requirement",
  tags=["requirement"]
  )
api_router.include_router(
  functional_document.router, 
  prefix="/document/functional",
  tags=["functional"]
  )
api_router.include_router(
  project.router, 
  prefix="/project",
  tags=["project"]
  )