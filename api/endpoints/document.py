from fastapi import APIRouter, Depends, HTTPException, Request
from schemas.document import ProductRequirementsDocumentRequest, ProductRequirementsDocument,DocumentIdResponse
from ai.product_requirement_document.prd_generator import generate_document
from mongo_db import init_db, db
import asyncio
from bson import ObjectId
from typing import List
router = APIRouter()

async def generate_requirement_document(requirement, db, db_object_id):
      print("generate document")
      document = generate_document(requirement)
      result = await db.requirement_document.update_one(
          {"_id":db_object_id},
          {"$set":{"document":document.model_dump(), "status":"finished"}}
      )
      print("generate finish")

@router.post("/requirement", response_model=DocumentIdResponse)
async def create_product_requirement_document(requirement: ProductRequirementsDocumentRequest, request: Request):
    db = request.app.state.db
    db_data = ProductRequirementsDocument(owner_id=requirement.owner_id, project_id=requirement.project_id,status="progress")
    db_object = await db.requirement_document.insert_one(db_data.model_dump())
    
    db_object_id = db_object.inserted_id
    # print(requirement)
    asyncio.create_task(generate_requirement_document(requirement.requirement,db,db_object_id))
    result = DocumentIdResponse(document_id=str(db_object_id))
    return result

@router.get("/requirement/project/{project_id}",response_model=List[ProductRequirementsDocument])
async def get_product_requirement_document(project_id: str, request : Request): 
    """
        프로젝트 id를 기반으로 요구사항정의서 목록을 mongodb에서 찾음
    """
    db = request.app.state.db
    documents = await db.requirement_document.find({"project_id":project_id}).to_list()
    if documents :
         return [ProductRequirementsDocument(**document) for document in documents]
    return None

@router.get("/requirement/{id}", response_model=ProductRequirementsDocument)
async def get_product_requirement_document(id: str, request : Request):
    """
    문서id를 기반으로 요구사항정의서를 mongodb에서 찾음
    """
    db = request.app.state.db
    document = await db.requirement_document.find_one({"_id":ObjectId(id)})
    if document :
         return ProductRequirementsDocument(**document)
    return ProductRequirementsDocument()

@router.delete("/requirement/{id}")
async def get_product_requirement_document(id: str, request : Request): 
    """
    문서id를 기반으로 요구사항정의서를 mongodb에서 삭제
    """
    db = request.app.state.db
    result  = await db.requirement_document.delete_one({"_id":ObjectId(id)})
    return {"msg":f"delete {result.deleted_count}"}
