import requests
from lxml import etree
from Classcjy import Chaojiying_Client

def getCodeText(imgPath):
    chaojiying = Chaojiying_Client('azb123 ', 'azb123', '914332')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imgPath, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    img_code = chaojiying.PostPic(im, 1902)['pic_str']
    return img_code

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
    img_code = getCodeText('./Code.jpg')
    print(img_code)