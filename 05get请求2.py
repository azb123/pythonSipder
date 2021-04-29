from urllib.request import urlopen,Request
from urllib.parse import urlencode

agre = {
    'wd':'尚学堂',
    'ie':'utf-8'
}
print(urlencode(agre))
url = "https://www.baidu.com/s?[]".format(urlencode(agre))

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

req = Request(url,headers=headers)
res = urlopen(req)
print(res.read().decode())