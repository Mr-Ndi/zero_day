from fastapi import FastAPI, Path, Request
from contextlib import asynccontextmanager
import uvicorn

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

@app.get("/")
async def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/hello{name}/{age}")
async def hello(name:str=Path(...,min_length=2), age:int=Path(...,gt=20)):
    return {"message": f"Hello I'm {name}, I am {age} years old!"}

if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1", port=3500, reload=True)