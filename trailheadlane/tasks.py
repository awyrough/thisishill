from celery import chord, group, chain
from thisishill import celery_app

from thisishill.loggers import logger

@celery_app.task
def add(x, y):
    logger.info("Adding %d and %d...", x, y)
    return x + y

def test_tasks():
    res = chain(add.s(2, 2), add.s(4), add.s(8))()
    res.get()
    return res