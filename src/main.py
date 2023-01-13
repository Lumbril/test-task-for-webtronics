from fastapi import FastAPI

from database import Base
from routers import test
from settings import engine


app = FastAPI()
app.include_router(test.test_api)

Base.metadata.create_all(bind=engine)
