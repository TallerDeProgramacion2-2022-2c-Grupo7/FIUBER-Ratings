from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import environ




POSTGRES_USER=environ.get("POSTGRES_USER")
POSTGRES_PASSWORD=environ.get("POSTGRES_PASSWORD")
POSTGRES_DB=environ.get("POSTGRES_DB")
PORT=environ.get("PORT")


DATABASE_URL = "postgresql://" + POSTGRES_USER + ":" + POSTGRES_PASSWORD  + "@localhost:" + PORT + "/" + POSTGRES_DB

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()