from fastapi import APIRouter, Depends, HTTPException, Request
from schemas.document import ServicePolicyDocumentRequest, FunctionalSpecificationDocument,DocumentIdResponse, ProductRequirementsDocument,ServicePolicyDocument
from ai.service_policy_document.spd_generator import generate_document
from mongo_db import init_db, db
import asyncio
from bson import ObjectId
from typing import List
router = APIRouter()

async def generate_policy_document(db, db_object_id, project_id):
      print("generate document spd")
      print(project_id)
      try:
        requirement =await db.requirement_document.find_one({"project_id" : project_id})
        requirement_data = ProductRequirementsDocument(**requirement)
        functional = await db.functional_document.find_one({"project_id": project_id})
        functional_data = FunctionalSpecificationDocument(**functional)

        document = await generate_document(requirement_data.document.metadata.requirement_summary, functional_data.document)
        result = await db.policy_document.update_one(
            {"_id":db_object_id},
            {"$set":{"document":document.model_dump(), "status":"finished"}}
        )
        print("generate finish")
      except Exception as err:
        print(err)
        await db.policy_document.update_one(
            {"_id":db_object_id},
            {"$set":{"status":"error"}}
        )

@router.post("/", response_model=DocumentIdResponse)
async def create_product_functional_document(requirement: ServicePolicyDocumentRequest, request: Request):
    try:
      db = request.app.state.db
      db_data = ServicePolicyDocument(owner_id=requirement.owner_id, project_id=requirement.project_id,status="progress")
      db_object = await db.policy_document.insert_one(db_data.model_dump())
      db_object_id = db_object.inserted_id
      # print(requirement)
      asyncio.create_task(generate_policy_document(db,db_object_id, requirement.project_id))
      result = DocumentIdResponse(document_id=str(db_object_id))
      return result
    except:
      pass
    return None

@router.delete("/{id}")
async def get_product_functional_document(id: str, request : Request): 
    """
    문서id를 기반으로 기능명세서를 mongodb에서 삭제
    """
    try:
        db = request.app.state.db
        result  = await db.policy_document.delete_one({"_id":ObjectId(id)})
        return {"msg":f"delete {result.deleted_count}"}
    except:
        pass
    return None

@router.get("/{id}", response_model=ServicePolicyDocument)
async def get_product_requirement_document(id: str, request : Request):
    """
    문서id를 기반으로 정책정의서를 mongodb에서 찾음
    """
    try:
        db = request.app.state.db
        document = await db.policy_document.find_one({"_id":ObjectId(id)})
        if document :
            return ServicePolicyDocument(**document)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Error")
