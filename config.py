import os
from dotenv import load_dotenv

load_dotenv()

# MySQL Database Configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "mysql+mysqlconnector://root:root@localhost:3306/pub"
)
