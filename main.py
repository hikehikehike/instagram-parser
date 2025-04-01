from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from core.crud import get_last_10_posts
from schemas.post import PostsResponse
from controllers.post_service import parse_new_post
from core.database import engine
from models.base import Base

app = FastAPI()


@app.get('/parse_posts', response_model=PostsResponse)
async def parse_posts(db: AsyncSession = Depends(get_db)):
    new_posts = await parse_new_post(db)
    if new_posts:
        return PostsResponse(posts=new_posts, message=None)
    return PostsResponse(posts=[], message='No new posts')


@app.get('/', response_model=PostsResponse)
async def read_posts(db: AsyncSession = Depends(get_db)):
    posts = await get_last_10_posts(db)
    if posts:
        return PostsResponse(posts=posts, message=None)
    return PostsResponse(posts=[], message='No posts found')


@app.on_event('startup')
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
