import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        for div in div_list:
            #注意伪属性
            img_url = 'https:' + div.xpath('./div/a/img/@src2').extract()[0]
            item = ImgsproItem(img_url=img_url)
            yield item
