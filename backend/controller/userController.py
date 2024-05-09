from fastapi import HTTPException, status
from auth.hashing import Hash
from auth.jwttoken import create_access_token
from bson import ObjectId
from config.config import db
from schemas.userSchemas import serializeDict, serializeList

def get_all_users():
    users = db.find()
    return serializeList(users)

def create_user_logic(user_data):
    hashed_pass = Hash.bcrypt(user_data.password)
    user_object = dict(user_data)
    user_object["password"] = hashed_pass
    user_id = db.insert_one(user_object).inserted_id
    return user_id

def authenticate_user(username, password):
    user = db.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user found with this {username} username')
    if not Hash.verify(user["password"], password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Wrong Username or password')
    access_token = create_access_token(data={"sub": user["username"]})
    return access_token
