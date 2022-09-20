from pydantic import BaseModel
from typing import Optional


class UserModel(BaseModel):
    id: Optional[int]
    username: str
    password: str


