import os

from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.get('DB_NAME', 'webtronics')
DB_USER = os.get('DB_USER', 'user')
DB_PASSWORD = os.get('DB_PASSWORD', 'password')
DB_HOST = os.get('DB_HOST', 'localhost')

SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
)
