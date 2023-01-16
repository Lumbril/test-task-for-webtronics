import uvicorn
from fastapi import FastAPI

from database.database import Base
from routers import test, registration, login, post, mark
from settings import engine


app = FastAPI()
app.include_router(test.test_api)
app.include_router(registration.registration_api)
app.include_router(login.login_api)
app.include_router(post.post_api)
app.include_router(mark.mark_api)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
