import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Remote MySQL Server Configuration
# Database connection details
# username = 'root'
# password = ''
# hostname = 'localhost'
# port = '3306'
# database_name = 'chat_application'
username = 'raihan'
password = 'Raihan%402025'
hostname = 'localhost'
port = '3306'
database_name = 'chat_application'

# Connect to MySQL database
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}:{port}/{database_name}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
