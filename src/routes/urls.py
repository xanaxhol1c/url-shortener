from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from src.dependencies import get_db
from src.schemas.urls import PostUrlRequest, PostUrlResponse, GetUrlRequest, GetUrlResponse
from src.services.urls import shorten_url
from src.crud.urls import get_url_by_slug

router = APIRouter()

@router.get('/')
def get_urls():
    return "Hello Url Shortener!"

@router.post(
    '/url', 
    response_model=PostUrlResponse,
    )
def post_url(request: PostUrlRequest, db = Depends(get_db)):
    slug = shorten_url(db, str(request.url))
    
    return PostUrlResponse(slug=slug)


@router.get(
    '/{url_slug}',
    response_model=GetUrlResponse
)
def get_url(url_slug: str, db = Depends(get_db)):
    url = get_url_by_slug(db, url_slug)

    if not url:
        raise HTTPException(
            status_code=404,
            detail={'message' : f'Url for slug = {url_slug} not found'}
        )
    
    return RedirectResponse(url=url.url)