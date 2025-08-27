from typing import Union
from fastapi import FastAPI
from routers import document
from mongo_db import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3100",
    "http://localhost:8181",
    "http://docgen-backend.aicc-project.com",
    "http://docgen.aicc-project.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db(app)
app.include_router(document.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}