from typing import Optional

from pydantic import BaseModel


class CommentModel(BaseModel):
    id:Optional[int]
    recipe_id: int
    user_id: int
    details: str
    DATE: str
