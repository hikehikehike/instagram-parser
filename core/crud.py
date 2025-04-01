import jmespath
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import desc
from models.post import Post
from schemas.post import PostBase


async def create_posts(db: AsyncSession, posts_data: list):
    result = await db.execute(select(Post.insta_post_id))
    existing_post_ids = {post_id for (post_id,) in result.all()}

    new_posts = []
    for post in posts_data:
        node = post.get('node', {})
        insta_post_id = node.get('code')

        if insta_post_id in existing_post_ids:
            continue

        text = jmespath.search('caption.text', node) or ''
        like_count = node.get('like_count', 0)
        comment_count = node.get('comment_count', 0)
        hashtag = '#Astronomy' in text

        new_posts.append(Post(
            insta_post_id=insta_post_id,
            text=text,
            like_count=like_count,
            comment_count=comment_count,
            hashtag=hashtag
        ))

    if new_posts:
        db.add_all(new_posts)
        await db.commit()
        return [PostBase.from_orm(post) for post in new_posts]

    return []


async def get_last_10_posts(db: AsyncSession):
    result = await db.execute(select(Post).order_by(desc(Post.id)).limit(10))
    posts = result.scalars().all()
    return [PostBase.from_orm(post) for post in posts]
