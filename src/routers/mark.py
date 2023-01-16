from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import crud
from database.database import get_db
from database.models import UserModel
from database.schemas import LikeSchema, LikeCreateSchema, LikeBaseSchema
from services.token import get_active_user_by_token


mark_api = APIRouter(prefix='/post/marks', tags=['Posts', 'Marks (likes and dislikes)'])


@mark_api.post('', response_model=LikeSchema)
def create_mark(mark: LikeCreateSchema, user: UserModel = Depends(get_active_user_by_token),
                db: Session = Depends(get_db)):
    post = crud.get_post(db, mark.post)

    if post is None:
        raise HTTPException(status_code=400, detail='Post is not exists')

    if post.author == user.id:
        raise HTTPException(status_code=400, detail='You can not rate your own posts')

    if crud.get_mark_by_user(db, mark.post, user.id):
        raise HTTPException(status_code=400, detail='Mark is exists')

    return crud.create_mark(db, mark, user)


@mark_api.get('/{post_id}', response_model=List[LikeSchema])
def get_marks(post_id: int, db: Session = Depends(get_db)):
    return crud.get_marks(db, post_id)


@mark_api.put('/{post_id}', response_model=LikeSchema)
def update_mark(post_id: int, data: LikeBaseSchema, user: UserModel = Depends(get_active_user_by_token),
                db: Session = Depends(get_db)):
    post = crud.get_post(db, post_id)

    if post is None:
        raise HTTPException(status_code=400, detail="Post is not exists")

    if post.author == user.id:
        raise HTTPException(status_code=400, detail='You can not rate your own posts')

    mark = crud.get_mark_by_user(db, post_id, user.id)

    if mark is None:
        raise HTTPException(status_code=400, detail="Mark is not exists")

    return crud.update_mark(db, mark, data, post_id, user.id)


@mark_api.delete('/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_mark(post_id: int, user: UserModel = Depends(get_active_user_by_token),
                db: Session = Depends(get_db)):
    if crud.get_post(db, post_id) is None:
        raise HTTPException(status_code=400, detail="Post is not exists")

    if crud.get_mark_by_user(db, post_id, user.id) is None:
        raise HTTPException(status_code=400, detail="Mark is not exists")

    crud.delete_mark(db, post_id, user.id)

    return None


@mark_api.get('/likes/{post_id}')
def get_count_likes(post_id: int, db: Session = Depends(get_db)):
    return crud.get_count_likes(db, post_id)


@mark_api.get('/dislikes/{post_id}')
def get_count_dislikes(post_id: int, db: Session = Depends(get_db)):
    return crud.get_count_dislikes(db, post_id)
