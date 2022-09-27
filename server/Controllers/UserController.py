from fastapi import APIRouter, Path
from logging import getLogger
from Models.UserModel import UserModel


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
async def get_user_by_id(user_id: int = Path(description="Enter the ID of User you want to get: ", gt=0)):
    if user_id not in users:
        return {"ERROR": "User Doesnot exists"}

    logger.info(f"fetching user for for {user_id}")
    return users[user_id]


@router.post("/CreateUser")
async def create_user(user: UserModel):
    logger.info("Creating new user")
    if user.username == None:
        return {"Enter a valid Username"}

    if user.username.isspace() == True:
        return {"ENTER A VALID USERNAME"}

    if user.username == "":
        return {"ENTER A VALID USERNAME"}

    if user.password.isspace() == True:
        return {"Password cannot cantain white spaces"}

    if user.password == "":
        return {"ENTER A VALID PASSWORD"}
    logger.debug(f"user is {user}")
    user_id = len(users)+1
    users[user_id] = user
    return users[user_id]


@router.put("/Update_user/{user_id}")
async def update_user(user: UserModel, user_id: int = Path(description="enter th eId of User You want to update", gt=0)):
    if user_id not in users:
        return {"ERROR": "User does not exists"}

    if user.username != None:
        users[user_id]['username'] = user.username

    if user.username.isspace() == True:
        return {"ENTER A VALID USERNAME"}

    if user.username == "":
        return {"ENTER A VALID USERNAME"}

    if user.password.isspace() == True:
        return {"Password cannot cantain white spaces"}

    if user.password == "":
        return {"ENTER A VALID PASSWORD"}

    if user.password != None:
        users[user_id]['password'] = user.password

    logger.debug(f"update the user for id = {user_id}, user = {user}")
    return users[user_id]


@router.delete("/delete_user/{user_id}")
def delete_user(user_id: int = Path(description="enter th Id of User You want to delete", gt=0)):
    if user_id not in users:
        return {"Error": "User doesnot Exists"}

    del users[user_id]
    logger.info(f"User with id = {user_id} has been deleted")
    return f"User with id = {user_id} has been deleted"
