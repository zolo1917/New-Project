
from copyreg import constructor
from typing_extensions import Self
from pydantic import BaseModel
from typing import Optional



class UserModel(BaseModel):
    username: Optional[str]
    password: str
