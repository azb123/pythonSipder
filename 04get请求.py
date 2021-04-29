from urllib.request import Request,urlopen
from urllib.parse import quote

url1 = 'https://www.baidu.com/s?wd={}'.format(quote('社区'))
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

request = Request(url1,headers=headers)
response = urlopen(request)
print(response.read().decode())