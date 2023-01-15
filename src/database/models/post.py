from sqlalchemy import Column, Integer, String, ForeignKey

from database.database import Base
from database.models import UserModel


class PostModel(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    text = Column(String)
    author = Column(ForeignKey(UserModel.id, ondelete='SET NULL'))
