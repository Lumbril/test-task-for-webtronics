import os

from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv('DB_NAME', 'webtronics')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_HOST = os.getenv('DB_HOST', 'localhost')

SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
)
