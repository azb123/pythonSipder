import requests
import re
#
# obj = re.compile(r"url: '(?P<url>.*?)',",re.S)
# url = 'https://www.91kanju.com/vod-play/54812-1-2.html'
#
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
#
# resp = requests.get(url=url,headers=headers).text
#
# m3u8_url = obj.search(resp).group("url")
#
# print(m3u8_url)
#
# #下载m3u8文件
#
# resp2 = requests.get(url=m3u8_url,headers=headers)
# with open("哲仁王后.m3u8",mode='wb') as fp:
#     fp.write(resp2.content)
n = 1
with open("哲仁王后.m3u8",mode='r',encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        if line.startswith("#"):
            continue
        if n<10:

            temp = '0' + '0' + str(n)
        elif 10<=n<100:
            temp = '0' + str(n)
        resp3 = requests.get(url=line,headers=headers)
        f = open(f"video/{temp}.ts",mode='wb')
        f.write(resp3.content)
        f.close()
        resp3.close()
        n+=1
        print(temp)