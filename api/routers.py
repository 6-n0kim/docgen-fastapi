from fastapi import APIRouter
from .endpoints import requirement_document

api_router = APIRouter()
api_router.include_router(
  requirement_document.router, 
  prefix="/document/requirement",
  tags=["requirement"]
  )
