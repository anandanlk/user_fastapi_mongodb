from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from models.userModel import User
from auth.oauth import get_current_user
from controller.userController import *


# Creating a router for user endpoints
user = APIRouter(prefix='/user')

@user.get("/")
def read_root(current_user: User = Depends(get_current_user)):
    return {"data": "Hello World"}

@user.post('/register')
def create_user(request: User):
    create_user_logic(request)
    return {"res": "created"}

@user.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends()):
    access_token = authenticate_user(request.username, request.password)
    return {"access_token": access_token, "token_type": "bearer"}

@user.get("/all", response_model=List[User])
def list_users(current_user: User = Depends(get_current_user)):
    return get_all_users()