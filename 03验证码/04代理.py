import requests

if __name__ == '__main__':
    url = 'http://www.baidu.com/s?ie=utf-8&wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    index_text = requests.get(url=url,headers=headers,proxies={'http':'60.169.148.252'}).text
    with open('./daili.html','w',encoding='utf-8') as fp:
        fp.write(index_text)
    print('over!!')