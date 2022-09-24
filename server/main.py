'''
    This is my main applcaiton file and its going to contain the application start code.
'''


# Each applciation
from fastapi import FastAPI
from Controllers import UserController,CommentsController
import logging
from database import getDBString
from dotenv import load_dotenv
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

getDBString()

app = FastAPI()

app.include_router(UserController.router)
app.include_router(CommentsController.router)


@app.get("/")
async def mainPage():
    return {"message": "I am awake"}

if __name__ == "__main__":
    print("This app is running")
