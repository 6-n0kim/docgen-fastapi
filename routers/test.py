from fastapi import APIRouter, Depends, HTTPException, Request
from models import TestModel, TestModelInDB
from mongo_db import init_db, db

router = APIRouter(
    prefix="/tests",
    tags=["tests"]
)

@router.post("/", response_model=TestModel)
async def create_user(test: TestModel, request: Request):
    db = request.app.state.db
    result = await db.tests.insert_one(test.dict())
    return TestModelInDB(id=str(result.inserted_id), **test.dict())

@router.get("/", response_model=list[TestModelInDB])
async def list_users(request: Request):
    db = request.app.state.db
    tests = await db.tests.find().to_list(100)
    return [TestModelInDB(id=str(u["_id"]), test_name=u["test_name"], description=u["description"]) for u in tests]

@router.get("/check")
async def check_api(request: Request):
    return {"msg":"hi"}