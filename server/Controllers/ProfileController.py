from Models.ProfileModel import ProfileModel
from fastapi import APIRouter
import logging

logging.basicConfig(level=logging)

router = APIRouter(prefix="/Profile")

users = [{"user_id": 1, "first_name": "test1", "last_name": "test1123", "contact_no": "1234", "address": "test1"},
         {"user_id": 2, "first_name": "test2", "last_name": "test1123",
             "contact_no": "5678", "address": "test2"},
         {"user_id": 3, "first_name": "test3", "last_name": "test1123",
             "contact_no": "9012", "address": "test3"},
         {"user_id": 4, "first_name": "test4", "last_name": "test1123", "contact_no": "3456", "address": "test4"}]


@router.get("/getAllUsers")
def get_users():
    logging.info("getting all users")
    return users


@router.get("/getuserbyid/{id}")
async def get_user_by_id(id):
    logging.info(f"fetching user for for {id}")
    return users[int(id)-1]


@router.post("/createuser")
async def create_user(user: ProfileModel):
    logging.info("Creating new user")
    print(user)
    logging.debug(f"user is {user}")
    return "User was created successfully"


@router.put("/updateuser")
async def update_user():
    pass


@router.delete("/deleteuser")
async def delete_user():
    pass
