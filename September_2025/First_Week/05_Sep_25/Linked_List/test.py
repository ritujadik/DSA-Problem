from fastapi import FastAPI
from pydantic import BaseModel
import bycrypt

app = FastAPI()


class User_Register(BaseModel):
    name:str
    email:email
    phone:int
    password:password



@app.post('/register')
def user_register(user_detail:User_Register):
    name = user_detail.name
    phone = user_detail.phone
    email = user_detail.email
    password = user_detail.password

    if len(phone) != 0:
        return("Please enter a correct phone number")








