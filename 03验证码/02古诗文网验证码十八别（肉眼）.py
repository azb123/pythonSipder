import requests
from lxml import etree



if __name__ == '__main__':
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    img_url = 'https://so.gushiwen.cn/'+tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data = requests.get(url=img_url,headers=headers).content
    with open('./Code.jpg','wb') as fp:
        fp.write(img_data)
    img_code = input('请输入验证码：')
    print(img_code)