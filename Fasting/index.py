from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/hello")
def hello(name:str, age:int):
    return {"message": f"Hello I'm {name}, I am {age} years old!"}

if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1", port=3500, reload=True)