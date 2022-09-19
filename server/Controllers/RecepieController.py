
from fastapi import APIRouter
from logging import getLogger



logger = getLogger(__name__)
router = APIRouter(prefix="/user")

recepie = {
   1:{
      "user_id": 11,
      "recipe_name":"pao_bhaji",
      "recipe_description":"punjabi new style pao bhaji",
      "created_date":"2020",
      "last_modified_date":'2021'
   },
   2:{
      "user_id":12,
      "recipe_name":"chhole bhatura",
      "recipe_description":"punjabi chhole bhature",
      "created_date":'2021',
      "last_modified_date":'2022'
   }
}

@router.get("/getRecepieById/{recepie_id}")
async def get_recepie_by_id(recepie_id):
    logger.info(f"fetching recepie for {recepie_id}")
    for recepie_id in recepie:     
        if recepie[recepie_id] == recepie_id:
            return recepie[recepie_id]
    return {"Data": "Not found"}


@router.get("/getAllRecepie")
async def get_all_recepie():
    logger.info("getting all recepie")
    return recepie