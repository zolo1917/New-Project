from fastapi import APIRouter
from logging import getLogger

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
    "3":{
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
