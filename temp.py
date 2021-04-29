import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
}


def download_code(s):
    url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    r = s.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    # 得到图片链接
    image_src = 'https://so.gushiwen.org' + soup.find('img', id='imgCode')['src']
    # print(image_src) # https://so.gushiwen.org/RandCode.ashx
    r_image = s.get(image_src,headers=headers)
    with open('code.png', 'wb') as fp:
        fp.write(r_image.content)

    # 表单所需要的两个参数
    __VIEWSTATEGENERATOR = soup.find('input', id='__VIEWSTATEGENERATOR')['value']
    __VIEWSTATE = soup.find('input', id='__VIEWSTATE')['value']
    return __VIEWSTATEGENERATOR, __VIEWSTATE


def login(viewg, view, s):
    post_url = 'https://so.gushiwen.org/user/login.aspx?from='
    # 提示用户输入验证码
    code = input("请输入验证码：")
    formdata = {
        'pwd': 'azb123',
        'from': '',
        'email': '438708212@qq.com',
        'denglu	': '登录',
        'code': code,
        '__VIEWSTATEGENERATOR': viewg,
        '__VIEWSTATE': view,
    }
    r = s.post(url=post_url, headers=headers, data=formdata)
    with open('古诗.html', 'w', encoding='utf8') as fp:
        fp.write(r.text)


def main():
    # 创建会话
    s = requests.Session()
    # 下载验证码到本地
    viewg,view = download_code(s)
    # 向post地址发送请求
    login(viewg, view, s)


if __name__ == '__main__':
    main()
