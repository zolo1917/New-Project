from pydantic import BaseModel


class CommentModel(BaseModel):
    id:int
    recipe_id: int
    user_id: int
    details: str
    DATE: str
