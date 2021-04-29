import scrapy
from selenium import webdriver

class BossSpider(scrapy.Spider):
    name = 'boss'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python']

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path=r"E:\google\Chrome\Application\chromedriver.exe")

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        print(li_list)
        for li in li_list:
            job_name = li.xpath('.//div[@class="job-title/span[1]/a//text()"]').extract()
            print(job_name)
            detail_url = 'https://www.zhipin.com/'+li.xpath('.//div[@class="job-title"]/span[1]/a/@href').extract_first()
