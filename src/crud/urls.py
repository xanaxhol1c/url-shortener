from sqlalchemy.orm import Session

from src.models.urls import Url

def get_url_by_slug(db: Session, slug: str):
    return db.query(Url).filter_by(slug=slug).first()

def get_url_by_original(db: Session, url: str):
    return db.query(Url).filter_by(url=url).first()

def create_url(db: Session, url: str, slug: str):
    new_url = Url(slug=slug, url=url)

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url