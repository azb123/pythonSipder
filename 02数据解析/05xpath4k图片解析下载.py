import requests,os
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'https://pic.netbian.com/4kmeinv/'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li/a')
    if not os.path.exists('./piclibs'):
        os.mkdir('./piclibs')
    for li in li_list:
        detail_url ='https://pic.netbian.com' + li.xpath('./img/@src')[0]
        detail_name = li.xpath('./img/@alt')[0]+'.jpg'
        detail_name = detail_name.encode('iso-8859-1').decode('GBK')
        detail_path = './piclibs/' + detail_name
        detail_data = requests.get(url=detail_url, headers=headers).content
        with open(detail_path,'wb') as fp:
            fp.write(detail_data)
            print(detail_name,'seccess!!')
