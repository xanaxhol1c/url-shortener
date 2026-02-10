from sqlalchemy import String, Column
from uuid import UUID

from .base import Base

class Url(Base):
    __tablename__ = "urls"

    slug = Column(String, primary_key=True)
    url = Column(String(500), nullable=False, index=True, unique=True)
    #created_at maybe in future
