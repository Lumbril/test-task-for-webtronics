from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import crud
from database.database import get_db
from database.models import UserModel
from database.schemas import PostSchema, PostCreateSchema
from services.token import get_active_user_by_token

post_api = APIRouter()


@post_api.get('/post', response_model=List[PostSchema])
def get_post_list(user: UserModel = Depends(get_active_user_by_token), db: Session = Depends(get_db)):
    return crud.get_posts_by_author(db, user.id)


@post_api.get('/post/{post_id}', response_model=PostSchema)
def get_post(post_id: int, user: UserModel = Depends(get_active_user_by_token), db: Session = Depends(get_db)):
    post = crud.get_post_by_author(db, post_id, user.id)

    if post is None:
        raise HTTPException(status_code=400, detail="Post is not exists")

    return post


@post_api.post('/post', response_model=PostSchema)
def create_post(data: PostCreateSchema, user: UserModel = Depends(get_active_user_by_token),
                db: Session = Depends(get_db)):
    return crud.create_post(db, data, user)


@post_api.put('/post/{post_id}', response_model=PostSchema)
def update_post(post_id: int, data: PostCreateSchema, user: UserModel = Depends(get_active_user_by_token),
                db: Session = Depends(get_db)):
    post = crud.get_post_by_author(db, post_id, user.id)

    if post is None:
        raise HTTPException(status_code=400, detail="Post is not exists")

    return crud.update_post(db, post, data)


@post_api.delete('/post/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, user: UserModel = Depends(get_active_user_by_token),
                db: Session = Depends(get_db)):

    if crud.get_post_by_author(db, post_id, user.id) is None:
        raise HTTPException(status_code=400, detail="Post is not exists")

    crud.delete_post(db, post_id)

    return None
