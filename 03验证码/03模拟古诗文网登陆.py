import requests
from lxml import etree

if __name__ == '__main__':
    #通过Session对象记录获取cookie
    session = requests.Session()
    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    #获取登录页面，并建立etree对象
    page_text = session.get(url=login_url,headers=headers).text
    tree = etree.HTML(page_text)
    #使用xpath解析验证码图片地址、动态属性
    img_url = 'https://so.gushiwen.cn/'+tree.xpath('//*[@id="imgCode"]/@src')[0]
    viewstate = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
    viewstategenerator = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
    #将验证码图片存储本地
    img_data = session.get(url=img_url,headers=headers).content
    with open('./Code.jpg','wb') as fp:
        fp.write(img_data)
    # 提示用户输入验证码
    img_code = input('请输入验证码：')
    data = {
        '__VIEWSTATE': viewstate,
        '__VIEWSTATEGENERATOR':viewstategenerator,
        'from':'http://so.gushiwen.cn/user/collect.aspx',
        'email': '438708212@qq.com',
        'pwd': 'azb123',
        'code': img_code,
        'denglu': '登录',
    }

    #post请求模拟登陆
    index = session.post(url=login_url, headers=headers, data=data)
    detial_url = 'https://so.gushiwen.cn/user/collectbei.aspx?sort=t'
    detial_text = session.get(url=detial_url,headers=headers).text
    with open('index.html', 'w', encoding='utf-8') as fp:
        fp.write(detial_text)
