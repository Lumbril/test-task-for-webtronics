from fastapi import FastAPI

from routers import test


app = FastAPI()
app.include_router(test.test_api)
