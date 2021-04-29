import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    model_urls = []
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path=r"E:\google\Chrome\Application\chromedriver.exe")
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3,4,6,7,8]
        for i in alist:
            model_url = li_list[i].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
        for url in self.model_urls:
            yield scrapy.Request(url,callback=self.model_parse)

    def model_parse(self,response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            if new_detail_url == None:
                continue
            item = WangyiproItem()
            item['title'] = title
            yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})
    def parse_detail(self,response):
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content
        yield item

    def closed(self,spider):
        self.bro.quit()

