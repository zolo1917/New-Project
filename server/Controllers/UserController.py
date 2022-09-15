from fastapi import APIRouter

router = APIRouter(prefix="/user")

users = [{"username": "test1", "password": "test1123"},
         {"username": "test1", "password": "test1123"},
         {"username": "test1", "password": "test1123"}]


@router.get("/getAllUsers")
def get_users():
    return users
