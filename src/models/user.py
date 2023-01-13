from sqlalchemy import Column, Integer, String, Boolean

from database import *


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String, )
    is_active = Column(Boolean, default=True)
