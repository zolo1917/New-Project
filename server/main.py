'''
    This is my main applcaiton file and its going to contain the application start code.
'''


# Each applciation

from fastapi import FastAPI
from Controllers import UserController
from logger_tt import setup_logging

setup_logging(full_context=1)
app = FastAPI()

app.include_router(UserController.router)


@app.get("/")
async def mainPage():
    return {"message": "I am awake"}

if __name__ == "__main__":
    print("This app is running")
