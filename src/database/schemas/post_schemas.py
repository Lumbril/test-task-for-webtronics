from pydantic import BaseModel


class PostCreateSchema(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True


class PostSchema(PostCreateSchema):
    id: int
    author: int
