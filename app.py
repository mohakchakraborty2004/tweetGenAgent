from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from greeting import greet

# const app = express()
app = FastAPI()

usersDB = {}

class USER(BaseModel):
    name : str
    age : int


@app.post("/register")
def reg_user(user: USER):
    usersDB[user.name] = user.age
    return {"message": greet(user.name), "data": user.dict()}

@app.get("/get-age")
def get_age(name): 
    age = usersDB[name]
    return {"message": "hello", "data": age}


