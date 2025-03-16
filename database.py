from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

conn=os.getenv("connection")
engine=create_engine(conn)

session=sessionmaker(bind=engine)

Base=declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
