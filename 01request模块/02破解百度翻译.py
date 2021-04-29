import requests
import json

if __name__ == '__main__':
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'
    }
    query = input('请输入需要翻译的内容：')
    data = {
        'kw':query
    }
    response = requests.post(url=url,data=data,headers=headers)
    dic_obj = response.json()
    fileName = query+'.json'

    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('保存成功！！')