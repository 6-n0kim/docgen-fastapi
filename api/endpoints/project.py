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

@router.get("/{project_id}")
async def find_document_list(project_id : str, request: Request):
    try:
      # print(project_id)
      db = request.app.state.db
      results = {}
      for col in collections:
        #  print(col)
         doc = await db[col].find_one(
            {"project_id":project_id},
            {"status":1, "create_date":1}
         )
        #  print(doc)
         if doc:
            results[col] = {
               "id" : str(doc["_id"]),
               "type" : col,
               "status" : doc["status"],
               "create_date": doc["create_date"]
            }
            # print(str(doc["_id"]))
      return results
    except:
      pass
    return None