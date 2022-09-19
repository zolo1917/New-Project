'''
    This is my main applcaiton file and its going to contain the application start code.
'''


# Each applciation

from fastapi import FastAPI
from Controllers import UserController
from Controllers import ProfileController
import logging
logging.basicConfig(level=logging.DEBUG)


app = FastAPI()
app.include_router(UserController.router)
app.include_router(ProfileController.router)


@app.get("/")
async def mainPage():
    return {"message": "I am awake"}

if __name__ == "__main__":
    print("This app is running")
