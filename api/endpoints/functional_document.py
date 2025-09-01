from fastapi import APIRouter, Depends, HTTPException, Request
from schemas.document import FunctionalSpecificationDocumentRequest, FunctionalSpecificationDocument,DocumentIdResponse, ProductRequirementsDocument
from ai.functional_specification_document.fsd_generator import generate_document
from mongo_db import init_db, db
import asyncio
from bson import ObjectId
from typing import List
router = APIRouter()

async def generate_functional_document(db, db_object_id, project_id):
      print("generate document fsd")
      print(project_id)
      requirement =await db.requirement_document.find_one({"project_id" : project_id})
      requirement_data = ProductRequirementsDocument(**requirement)
      document = generate_document(requirement_data.document)
      result = await db.functional_document.update_one(
          {"_id":db_object_id},
          {"$set":{"document":document.model_dump(), "status":"finished"}}
      )
      print("generate finish")

@router.post("/", response_model=DocumentIdResponse)
async def create_product_functional_document(requirement: FunctionalSpecificationDocumentRequest, request: Request):
    try:
      db = request.app.state.db
      db_data = FunctionalSpecificationDocument(owner_id=requirement.owner_id, project_id=requirement.project_id,status="progress")
      db_object = await db.functional_document.insert_one(db_data.model_dump())
      db_object_id = db_object.inserted_id
      # print(requirement)
      asyncio.create_task(generate_functional_document(db,db_object_id, requirement.project_id))
      result = DocumentIdResponse(document_id=str(db_object_id))
      return result
    except:
      pass
    return None