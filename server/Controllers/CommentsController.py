from logging import getLogger

from Models.CommentModel import CommentModel
from fastapi import APIRouter

logger = getLogger(__name__)
router = APIRouter(prefix="/comment")

comment = {
    "1": {
        "id": 11,
        "recipe_id": 123,
        "user_id": 5077,
        "details": " hellwo jarvish",
        "created_date": "2000",

    },
    "2": {
        "id": 12,
        "recipe_id": 32104,
        "user_id": 5002,
        "details": " jarvish is Here",
        "created_date": "1900",

    },
    "3": {
        "id": 14,
        "recipe_id": 48865,
        "user_id": 5345,
        "details": " jarvish is Everywere",
        "created_date": "2022",

    }
}


@router.get("/getCommentsById/{id}")
async def get_comment_by_id(id):
    logger.info(f" Comment  for {id}")
    print('Dict: ', id)

    if id in comment:
        return comment[id]
    else:
        return {"Data": "Not found"}


@router.get("/allComment")
async def get_all_comment():
    logger.info("getting all Comment")
    return comment


@router.post("/create_Comment")
async def create_comment(comment: CommentModel):
    logger.info("Creating new comment")
    logger.debug(f"user is {comment}")
    return "created Comment"


@router.put("/update_Comment")
async def update_comment(id, comment: CommentModel):
    logger.debug(f"update Comment by id {id}, Comment = {comment}")
    return f"update comment by id = {id}, Comment = {comment}"


@router.delete("/delete_Comment")
async def delete_comment(id):
    logger.info(f"Comment by id = {id} Deleted")
    return f" Comment id = {id} has been deleted"
