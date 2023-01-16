import enum

from sqlalchemy import Column, Integer, ForeignKey, Enum

from database.database import Base
from database.models import UserModel, PostModel


class TypeMark(enum.Enum):
    like = "Like"
    dislike = "Dislike"


class LikeModel(Base):
    __tablename__ = 'likes_and_dislikes'

    id = Column(Integer, primary_key=True, index=True)
    user = Column(ForeignKey(UserModel.id, ondelete='SET NULL'))
    post = Column(ForeignKey(PostModel.id, ondelete='CASCADE'))
    mark = Column(Enum(TypeMark))
