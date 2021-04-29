import requests


url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
kw = input('请输入想要查询的kfc地址：')
index = input('请输入想要查询的kfc地址第几页：')
data = {
    'cname':'',
    'pid':'' ,
    'keyword': kw,
    'pageIndex': index,
    'pageSize': '10'
}
response = requests.post(url=url,data=data,headers=headers)
kfc_data = response.text

fileName = kw+'kfc地址.txt'

with open(fileName, 'w', encoding='utf-8', ) as fp:
    fp.write(kfc_data)
print("over!!!")
