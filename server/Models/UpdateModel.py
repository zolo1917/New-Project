from pydantic import BaseModel
from typing import Optional

class UpdateModel(BaseModel):
    username: Optional[str]
    password: Optional[str]