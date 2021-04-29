import scrapy


class MiddlerSpider(scrapy.Spider):
    name = 'middler'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
