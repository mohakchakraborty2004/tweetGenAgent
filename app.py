from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from greeting import gen_tweet
from typing import List

# const app = express()
app = FastAPI()

usersDB = {}

class USER(BaseModel):
    name : str
    age : int

class TWEET(BaseModel):
    tasks : List[str]

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.post("/register")
def reg_user(user: USER):
    usersDB[user.name] = user.age
    return {"message": "hello", "data": user.dict()}

@app.post("/gen-tweet")
def get_tweet(data: TWEET): 
    return {"tweet" : gen_tweet(data)}
    


