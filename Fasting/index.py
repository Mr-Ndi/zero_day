from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import uvicorn
from Routes import book_routes
from handler import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

@app.get("/")
async def home():
    return {"message": "Welcome to the FastAPI application!"}

app.include_router(book_routes.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1", port=3500, reload=True)