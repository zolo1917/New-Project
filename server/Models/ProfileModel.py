from pydantic import BaseModel


class ProfileModel(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    contact_no: int
    address: str
