from fastapi import FastAPI, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/hello{name}/{age}")
async def hello(name:str=Path(...,min_length=2), age:int=Path(...,gt=20)):
    return {"message": f"Hello I'm {name}, I am {age} years old!"}

@app.get("/hello", response_class=HTMLResponse)
async def hello(request: Request):
    return templates.TemplateResponse("hello.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1", port=3500, reload=True)