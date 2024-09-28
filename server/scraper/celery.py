import os
from celery import Celery


celery_app = Celery(broker=os.getenv("CELERY_BROKER_URL"))


def task_scrap_products():
    """
    Schedule the product scraping task.
    """
    celery_app.send_task('app.main.task_scrap_products')
