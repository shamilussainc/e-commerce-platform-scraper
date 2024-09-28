import os, scrapy
from app.utils import send_product_to_server


class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = [
        os.getenv("SCRAPY_START_URL")+"?currentPage=1",
    ]

    def parse(self, response):            
        links = response.css('div.itemSearchBoxWrap > div > p.ttl > a::attr(href)').getall()

        for link in links:
            product_link = response.urljoin(link)
            yield response.follow(product_link, self.parse_product)

        # # Get the current page number from the URL
        # current_page = int(response.url.split('currentPage=')[-1])
        # next_page = current_page + 1
        # # Construct the next page URL
        # next_page_url = response.urljoin(f"{os.getenv('SCRAPY_START_URL')}?currentPage={next_page}")
        # # limiting number of pages for scrapping.
        # if next_page <= 10:
        #     yield scrapy.Request(next_page_url, callback=self.parse)


    def parse_product(self, response):
        product = {
            "title": response.css('div.itemDetailBox > h1::text').get(),
            "description": ''.join(response.css('div.itemDescription > p::text').getall()),
            "selling_status":  response.css('p.order > img').attrib['alt'] if response.css('p.order > img') else "Available",
            "product_condition": ''.join(response.css('td.RightItemDetail > div.itemState > p.state > span::text').getall()),
        }
        send_product_to_server(product)


