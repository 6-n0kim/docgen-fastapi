import os
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
print(MONGO_URI)
print(MONGO_DB)
client: AsyncIOMotorClient = None
db = None

def init_db(app: FastAPI):
    @app.on_event("startup")
    async def startup_event():
        global client, db
        client = AsyncIOMotorClient(MONGO_URI)
        db = client[MONGO_DB]
        app.state.db = db
        print(f"✅ MongoDB connected: {MONGO_URI}")

    @app.on_event("shutdown")
    async def shutdown_event():
        app.state.db.client.close()
        print("🛑 MongoDB disconnected")