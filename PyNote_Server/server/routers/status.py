from fastapi import APIRouter


router = APIRouter()


@router.get('/status')
async def server_get_status():
    return {'msg': 'All good'}