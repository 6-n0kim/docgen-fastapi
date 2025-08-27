from fastapi import APIRouter, Depends, HTTPException, Request
from models import ProductRequirementsDocumentRequest, ProductRequirementsDocument
from ai.product_requirement_document.prd_generator import Requirement_Document, generate_document
from mongo_db import init_db, db

router = APIRouter(
    prefix="/document",
    tags=["document"]
)

@router.post("/requirement", response_model=Requirement_Document)
async def create_product_requirement_document(requirement: ProductRequirementsDocumentRequest, request: Request):
    db = request.app.state.db
    # print(requirement)
    data = generate_document(requirement.requirement)
    result = await db.requirement_document.insert_one(data.dict())
    return data