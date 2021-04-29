import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    }
    page_text = requests.get(url=url,headers=headers).content.decode('utf-8')
    tree = etree.HTML(page_text)
    #热门城市   //div[@class="bottom"]/ul/li
    #全部城市   //div[@class="bottom"]/ul/div[2]/li
    a_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
    fp = open('./citys.txt','w',encoding='utf-8')
    i = 0
    for a in a_list:
        city_name = a.xpath('.//a/text()')[0]
        fp.write(city_name+'\t')
        i=i+1
        if i == 6:
            i = 0
            fp.write('\n')
    print('爬取成功')



