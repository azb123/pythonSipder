from urllib.request import urlopen,Request

url1 = "http://www.baidu.com"

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
req = Request(url1,headers=head)
print(req.get_header('User-agent'))

resp = urlopen(req)
info1 = resp.read()
print(info1.decode())