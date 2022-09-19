from fastapi import APIRouter,Path
from logging import getLogger
from Model.UserModel import UserModel
from Model.UpdateModel import UpdateModel

logger = getLogger(__name__)


router = APIRouter(prefix="/user")

users = {
        1: 
            {"username": "test1", 
            "password": "test1123"},
        2: 
            {"username": "test2",  
            "password": "test1123"},
        3: 
            {"username": "test3", 
            "password": "test1123"},
        4:
            {"username": "test4", 
            "password": "test1123"}}


@router.get("/getAllUsers")
async def get_users():
    logger.info("getting all users")
    return users

@router.get("/GetUserById/{user_id}")
async def get_user_by_id(user_id:int=Path(description="Enter the ID of User you want to get: ",gt=0) ):
    if user_id not in users:
        return {"ERROR":"User Doesnot exists"}
        
    logger.info(f"fetching user for for {user_id}")
    return users[user_id]

@router.post("/CreateUSer/{user_id}")
async def create_new_user(user_id: int, user: UserModel):
    logger.info("Creating new user")
    if user_id in users:
        return {"ERROR":"USER EXIXTS"}
    
    logger.debug(f"user is {user}")
    users[user_id]=user
    return users[user_id] 

@router.put("/Update_user/{user_id}")
async def update_user(user:UpdateModel,user_id: int=Path(description="enter th eId of User You want to update",gt=0)):
    if user_id not in users:
        return {"ERROR":"User does not exists"}

    if user.username != None:
        users[user_id]['username']= user.username

    if user.password != None:
        users[user_id]['password']=user.password
    
    logger.debug(f"update the user for id = {user_id}, user = {user}")
    return users[user_id]

@router.delete("/delete_user/{user_id}")
def delete_user(user_id: int=Path(description="enter th Id of User You want to delete",gt=0)):
    if user_id not in users:
        return {"Error":"User doesnot Exists"}
    
    del users[user_id]
    logger.info(f"User with id = {user_id} has been deleted")
    return f"User with id = {user_id} has been deleted"

    


