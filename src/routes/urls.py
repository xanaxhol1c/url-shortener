from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from typing import Annotated
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.schemas.urls import PostUrlRequest, PostUrlResponse
from src.services.urls import shorten_url
from src.crud.urls import get_url_by_slug

router = APIRouter()


@router.get("/")
def get_urls() -> str:
    return "Hello Url Shortener!"


@router.post("/url")
def post_url(request: PostUrlRequest, db: Annotated[Session, Depends(get_db)]) -> PostUrlResponse:
    slug = shorten_url(db, str(request.url))

    return PostUrlResponse(slug=slug)


@router.get("/{url_slug}")
def get_url(url_slug: str, db: Annotated[Session, Depends(get_db)]) -> RedirectResponse:
    url = get_url_by_slug(db, url_slug)

    if not url:
        raise HTTPException(
            status_code=404, detail={"message": f"Url for slug = {url_slug} not found"}
        )

    return RedirectResponse(url=url.url)
