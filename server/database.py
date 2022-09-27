from os import environ as env
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

user = env.get("local.db.user")
password = env.get("local.db.password")
host = env.get("local.db.host")
port = env.get("local.db.port")
database = env.get("local.db.database")

SQL_SESSION_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(SQL_SESSION_URL, echo=True)

SessionLocal = sessionmaker(autoflush=False, autocommit=True, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        db.begin()
        yield db
    finally:
        db.close()
