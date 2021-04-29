from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = 'https://www.gulongwang.com/duo/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).content.decode('GBK')
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.lb > ul > li')
    fp = open('./多情剑客无情剑.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.gulongwang.com/'+li.a['href']
        detail_page_text = requests.get(url=detail_url,headers=headers).content.decode('GBK')
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div', class_='nr_con')
        content = div_tag.text
        fp.write('\n'+title+content+'\n')
        print(title,'爬取成功')
