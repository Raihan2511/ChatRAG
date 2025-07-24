import os
from dotenv import load_dotenv

load_dotenv()

# MySQL Database Configuration
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")
