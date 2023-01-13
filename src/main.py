from fastapi import FastAPI

from database.database import Base
from routers import test, registration, login
from settings import engine


app = FastAPI()
app.include_router(test.test_api)
app.include_router(registration.registration_api)
app.include_router(login.login_api)

Base.metadata.create_all(bind=engine)
