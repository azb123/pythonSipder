import scrapy
from meinvNetwork.items import MeinvnetworkItem

class MnspiderSpider(scrapy.Spider):
    name = 'mnSpider'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']
    url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 2
    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div[2]/div[2]/ul/li')
        for li in li_list:
            name = li.xpath('./a[2]/b/text() | ./a[2]/text()').extract_first()
            item = MeinvnetworkItem(name=name)
            yield item
        if self.page_num <= 11:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url,callback=self.parse)