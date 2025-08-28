from fastapi import APIRouter, Depends, HTTPException, Request
from schemas.document import ProductRequirementsDocumentRequest, ProductRequirementsDocument
from ai.product_requirement_document.prd_generator import generate_document
from mongo_db import init_db, db
import asyncio
router = APIRouter()

async def generate_requirement_document(requirement, db, db_object_id):
      print("generate document")
      document = generate_document(requirement)
      result = await db.requirement_document.update_one(
          {"_id":db_object_id},
          {"$set":{"document":document.model_dump(), "status":"finished"}}
      )

@router.post("/", response_model=ProductRequirementsDocument)
async def create_product_requirement_document(requirement: ProductRequirementsDocumentRequest, request: Request):
    db = request.app.state.db
    db_data = ProductRequirementsDocument(owner_id=requirement.owner_id, project_id=requirement.project_id,status="progress")
    db_object = await db.requirement_document.insert_one(db_data.model_dump())
    db_object_id = db_object.inserted_id
    # print(requirement)

    
    asyncio.create_task(generate_requirement_document(requirement.requirement,db,db_object_id))
    
    return db_data