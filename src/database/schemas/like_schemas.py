from pydantic import BaseModel

from database.models import TypeMark


class LikeBaseSchema(BaseModel):
    mark: TypeMark

    class Config:
        orm_mode = True


class LikeCreateSchema(LikeBaseSchema):
    post: int


class LikeSchema(LikeCreateSchema):
    user: int
