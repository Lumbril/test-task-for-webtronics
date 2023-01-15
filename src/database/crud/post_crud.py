from sqlalchemy.orm import Session

from database import models, schemas
from database.models import UserModel


def get_post(db: Session, post_id: int):
    return db.query(models.PostModel).filter(models.PostModel.id == post_id).first()


def get_post_by_author(db: Session, author: str):
    return db.query(models.PostModel).filter(models.PostModel.author == author).first()


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PostModel).offset(skip).limit(limit).all()


def create_post(db: Session, post: schemas.PostCreateSchema, author: UserModel):
    db_post = models.PostModel(title=post.title, text=post.text, author=author.id)

    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post
