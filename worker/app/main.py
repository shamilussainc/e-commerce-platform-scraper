import logging, os
from celery import Celery
from scrapy.crawler import CrawlerProcess
from app.web_crawler import ProductsSpider


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Celery(main='scrap_worker', broker=os.getenv("CELERY_BROKER_URL"))


@app.task
def task_scrap_products():
    try:
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        process.crawl(ProductsSpider)

        logger.info("Starting Scrapy process for product scraping.")
        process.start(stop_after_crawl=False)
    except Exception as e:
        logger.error(f"Error during the scraping process: {e}")
        raise e
