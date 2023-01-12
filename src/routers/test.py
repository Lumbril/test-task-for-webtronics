from fastapi import APIRouter


test_api = APIRouter()


@test_api.get('/test/')
async def test():
    return {'message': 'Hello'}
