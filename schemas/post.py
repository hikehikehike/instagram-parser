from pydantic import BaseModel
from typing import List, Optional


class PostBase(BaseModel):
    insta_post_id: str
    text: str
    like_count: int
    comment_count: int
    hashtag: bool

    class Config:
        orm_mode = True
        from_attributes = True


class PostsResponse(BaseModel):
    posts: List[PostBase]
    message: Optional[str]

    class Config:
        orm_mode = True
