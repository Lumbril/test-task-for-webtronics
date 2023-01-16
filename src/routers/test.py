from fastapi import APIRouter, Depends

from database.models import UserModel
from database.schemas import UserSchema
from services.token import get_active_user_by_token

import redis


test_api = APIRouter(tags=['Test'])


@test_api.get('/test')
async def test():
    return {'message': 'Hello'}


@test_api.get('/test/me', response_model=UserSchema)
def me(user: UserModel = Depends(get_active_user_by_token)):
    return user


@test_api.get('/test/redis')
def test_redis():
    r = redis.Redis(host='redis')
    r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
    x = r.get("Bahamas")

    return x if x else 'bad'
