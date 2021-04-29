import random
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.116 Safari/537.36 ',
        'Referer': 'https://www.pearvideo.com/video_1724179',
    }

params = {
    'contId': '1724179',
    'mrd': str(random.random())
}

url = 'https://www.pearvideo.com/videoStatus.jsp'
response = requests.get(url=url, headers=headers, params=params)
data = response.json()
print(data)