from fastapi import APIRouter, Depends

from database.models import UserModel
from database.schemas import UserSchema
from services.token import get_active_user_by_token

test_api = APIRouter()


@test_api.get('/test')
async def test():
    return {'message': 'Hello'}


@test_api.get('/test/me', response_model=UserSchema)
def me(user: UserModel = Depends(get_active_user_by_token)):
    return user
