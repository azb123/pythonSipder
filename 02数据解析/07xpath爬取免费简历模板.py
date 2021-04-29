import requests,os
from lxml import etree

if __name__ == '__main__':
    url = 'https://sc.chinaz.com/jianli/free.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    }
    page_text = requests.get(url=url,headers=headers).content.decode('utf-8')
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@class="box col3 ws_block"]/a')
    if not os.path.exists('./简历模板'):
        os.mkdir('./简历模板')
    for a in a_list:
        detail_url = 'https:'+a.xpath('./@href')[0]
        detail_page_text = requests.get(url=detail_url,headers=headers).content.decode('utf-8')
        detail_tree = etree.HTML(detail_page_text)
        detail_a_list = detail_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a')
        for a in detail_a_list:
            download_name = detail_tree.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
            download_url = a.xpath('./@href')[0]
            download_data = requests.get(url=download_url,headers=headers).content
            download_path = './简历模板/'+download_name+'.rar'
            with open(download_path,'wb') as fp:
                fp.write(download_data)
                print(download_name,'success!!')
