from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_tables


@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield




app=FastAPI(title="Tic Tac Toe",lifespan=lifespan)

@app.get("/api/health")
def health_check():
    return {"status":"Ok"}