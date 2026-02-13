from pydantic import BaseModel, HttpUrl, Field


class PostUrlRequest(BaseModel):
    url: HttpUrl


class PostUrlResponse(BaseModel):
    slug: str = Field(..., max_length=8, min_length=1)


class GetUrlRequest(BaseModel):
    slug: str = Field(..., max_length=8, min_length=1)


class GetUrlResponse(BaseModel):
    url: HttpUrl
