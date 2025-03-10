
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

conn="postgresql://postgres:chetan@127.0.0.1:5432/User"

engine=create_engine(conn)

session=sessionmaker(bind=engine)

Base=declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
