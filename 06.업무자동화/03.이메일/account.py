import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")