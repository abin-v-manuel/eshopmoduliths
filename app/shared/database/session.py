import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()  # ✅ Important: Load the .env file

DATABASE_URL = os.getenv("DB_URL")  # ✅ Must match .env key

if not DATABASE_URL:
    raise ValueError("DB_URL not found in environment")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
