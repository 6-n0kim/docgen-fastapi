from fastapi import APIRouter, Depends, HTTPException, Request
from schemas.document import FunctionalSpecificationDocumentRequest, FunctionalSpecificationDocument,DocumentIdResponse, ProductRequirementsDocument,DocumentListInProject,DocumentListItemInProject
from ai.functional_specification_document.fsd_generator import generate_document
from mongo_db import init_db, db
import asyncio
from bson import ObjectId
from typing import List
router = APIRouter()

collections = [
  "requirement_document",
  "functional_document",
  "policy_document"
]

@router.get("/{user_id}")
async def find_document_list(user_id : str, request: Request):
    try:
      print(user_id)
      db = request.app.state.db
      results = []
      for col in collections:
        #  print(col)
         docs = await db[col].find(
            {"owner_id":user_id},
            {"status":1, "create_date":1, "project_id":1}
         ).to_list()
        #  print(doc)
         if docs:
            for doc in docs:
               results.append({
               "id" : str(doc["_id"]),
               "project_id" : doc["project_id"],
               "type" : col,
               "status" : doc["status"],
               "create_date": doc["create_date"]
              })
            # print(str(doc["_id"]))
      return results
    except Exception as e:
      raise HTTPException(status_code=400, detail=f"처리 실패: {str(e)}")