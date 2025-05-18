confing.py
import os

class Config:
    API_KEY = os.getenv("API_KEY")
    DB_URI = os.getenv("DB_URI")
    EMAIL = os.getenv("EMAIL")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
