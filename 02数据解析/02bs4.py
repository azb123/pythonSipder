from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url,headers=headers).content.decode('utf-8')
    soup = BeautifulSoup(page_text,'lxml')
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./三国演义小说.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        detail_page_text = requests.get(url=detail_url,headers=headers).content.decode('utf-8')
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        content = div_tag.text
        fp.write('\n' + title + ':' + content +'\n')
        print(title,'爬取成功')
