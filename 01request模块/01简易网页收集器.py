import requests
if __name__ == '__main__':
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = 'https://www.sogou.com/sie'
    kw = input("请输入需要搜索的内容：")
    param = {
        'query':kw
    }
    response = requests.get(url=url,params=param,headers=head)
    page_text = response.text
    filename = kw + '.html'
    with open(filename,'w',encoding='utf-8',) as fp:
        fp.write(page_text)
    print(filename,'保存成功！！')