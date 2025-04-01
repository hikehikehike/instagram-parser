from celery import Celery

from celery.schedules import crontab

celery_app = Celery(
    'tasks',
    broker='redis://redis:6379/0',
    backend='redis://redis:6379/0',
)


@celery_app.task
def parse_posts_task():
    from controllers.post_service import parse_new_post
    from core.database import SessionLocal

    db = SessionLocal()
    parse_new_post(db)
    db.close()


celery_app.conf.beat_schedule = {
    'parse-every-10-minutes': {
        'task': 'tasks.celery_app.parse_posts_task',
        'schedule': crontab(minute='*/10'),
    },
}
