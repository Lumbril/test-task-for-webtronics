from sqlalchemy.orm import Session

from database import models
from database.models import UserModel
from database.schemas import LikeCreateSchema, LikeBaseSchema


def get_marks(db: Session, post_id: int):
    return db.query(models.LikeModel).filter(models.LikeModel.post == post_id).all()


def get_count_likes(db: Session, post_id: int):
    return len(db.query(models.LikeModel).filter(models.LikeModel.post == post_id,
                                                 models.LikeModel.mark == models.TypeMark.like).all())


def get_count_dislikes(db: Session, post_id: int):
    return len(db.query(models.LikeModel).filter(models.LikeModel.post == post_id,
                                                 models.LikeModel.mark == models.TypeMark.dislike).all())


def get_mark_by_user(db: Session, post_id: int, user: int):
    return db.query(models.LikeModel).filter(models.LikeModel.post == post_id,
                                             models.LikeModel.user == user).first()


def create_mark(db: Session, like: LikeCreateSchema, user: UserModel):
    db_mark = models.LikeModel(user=user.id, post=like.post, mark=like.mark)

    db.add(db_mark)
    db.commit()
    db.refresh(db_mark)

    return db_mark


def update_mark(db: Session, like: LikeBaseSchema, post_id: int, user: UserModel):
    update_data = like.dict(exclude_unset=True)


def delete_mark(db: Session, post_id: int, user: UserModel):
    db_mark = get_mark_by_user(db, post_id, user.id)

    db.delete(db_mark)
    db.commit()

    return db_mark
