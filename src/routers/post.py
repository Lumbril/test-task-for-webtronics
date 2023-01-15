from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import crud
from database.database import get_db
from database.models import UserModel
from database.schemas import PostSchema, PostCreateSchema
from services.token import get_active_user_by_token

post_api = APIRouter()


@post_api.post('/post', response_model=PostSchema)
def create_post(data: PostCreateSchema, user: UserModel = Depends(get_active_user_by_token),
                db: Session = Depends(get_db)):
    return crud.create_post(db, data, user)
