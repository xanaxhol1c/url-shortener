import random
import string
from sqlalchemy.orm import Session
from src.crud.urls import get_url_by_original, create_url


def generate_slug(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


def shorten_url(db: Session, url: str) -> str:
    existing_url = get_url_by_original(db, url)

    if existing_url:
        return existing_url.slug

    slug = generate_slug()

    new_url = create_url(db, url, slug)

    return new_url.slug
