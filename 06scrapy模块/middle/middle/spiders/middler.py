import scrapy
import time

class MiddlerSpider(scrapy.Spider):
    name = 'middler'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        time.sleep(2)
        page_text = response.text
        time.sleep(2)
        with open('./ip.html','w',encoding='utf-8') as fp:
            fp.write(page_text)
