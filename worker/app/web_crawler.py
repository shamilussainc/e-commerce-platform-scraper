import os, scrapy
from app.utils import send_product_to_server


class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = [
        os.getenv("SCRAPY_START_URL"),
    ]

    def parse(self, response):            
        links = response.css('div.itemSearchBoxWrap > div > p.ttl > a::attr(href)').getall()

        for link in links:
            product_link = response.urljoin(link)
            yield response.follow(product_link, self.parse_product)


    def parse_product(self, response):
        product = {
            "title": response.css('div.itemDetailBox > h1::text').get(),
            "description": ''.join(response.css('div.itemDescription > p::text').getall()),
            "selling_status":  response.css('p.order > img').attrib['alt'] if response.css('p.order > img') else "Available",
            "product_condition": ''.join(response.css('td.RightItemDetail > div.itemState > p.state > span::text').getall()),
        }
        send_product_to_server(product)
