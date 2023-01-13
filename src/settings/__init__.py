import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

if os.getenv("LEVEL") == "PROD":
    from .prod import *
    print('RUN PROD MODE')
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    from .local import *
    print('RUN LOCAL MODE')
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

