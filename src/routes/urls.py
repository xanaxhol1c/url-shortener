from fastapi import APIRouter, Depends
from src.dependencies import get_db
from src.schemas.urls import PostUrlRequest, PostUrlResponse, GetUrlRequest

router = APIRouter()

@router.get('/')
def get_urls():
    return "Hello Url Shortener!"

@router.post(
    '/url', 
    response_model=PostUrlResponse,
    )
def post_url(request: PostUrlRequest, db = Depends(get_db)):
    ...

@router.post('/{url_slug}')
def get_url_by_slug(request: GetUrlRequest, url_slug: str, db = Depends(get_db)):
    return {'slug' : str(url_slug)}
