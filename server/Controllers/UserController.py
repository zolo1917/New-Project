from Models.UserModel import UserModel
from fastapi import APIRouter
from logger_tt import logger
from logger_tt import setup_logging

setup_logging(full_context=1)

router = APIRouter(prefix="/user")

users = [{"id": 1, "username": "test1", "password": "test1123"},
         {"id": 2, "username": "test2", "password": "test1123"},
         {"id": 3, "username": "test3", "password": "test1123"},
         {"id": 4, "username": "test4", "password": "test1123"}]


@router.get("/getAllUsers")
def get_users():
    logger.info("getting all users")
    return users


@router.get("/getuserbyid/{id}")
async def get_user_by_id(id):
    logger.info(f"fetching user for for {id}")
    return users[int(id)-1]


@router.post("/createuser")
async def create_user(user: UserModel):
    logger.info("Creating new user")
    print(user)
    logger.debug(f"user is {user}")
    return "User was created successfully"


@router.put("/updateuser")
async def update_user():
    pass


@router.delete("/deleteuser")
async def delete_user():
    pass
