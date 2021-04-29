import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

param = {
    'type': '5',
    'interval_id': '100:90',
    'action':'',
    'start': '0',
    'limit': '20'
}
response = requests.get(url=url,params=param,headers=headers)
list_data = response.json()

fileName = 'douban.json'
fp = open(fileName,'w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
