import scrapy
from qiushi.items import QiushiItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # def parse(self, response):
    #     div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
    #     all_data = []
    #     for div in div_list:
    #         #xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         #extract可以将Selector对象中的data参数存储的字符串提取出来
    #
    #         #author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         author  = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         content = div.xpath('./a[1]/div/span/text()').extract()
    #         content = ''.join(content)
    #         dic = {
    #             'author':author,
    #             'content':content
    #         }
    #         all_data.append(dic)
    #     return all_data
    #('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')
    def parse(self, response):
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        all_data = []
        for div in div_list:
            #xpath返回的是列表，但是列表元素一定是Selector类型的对象
            #extract可以将Selector对象中的data参数存储的字符串提取出来

            #author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span/text()').extract()
            content = ''.join(content)

            item = QiushiItem(author=author, content=content)
            # item['author'] = author
            # item['content'] = content

            yield item