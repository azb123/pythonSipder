import requests
import re
import os


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    if not os.path.exists('./qiushi'):
        os.mkdir('./qiushi')
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for pageNum in range(1,3):
        new_url = format(url%pageNum)

        gate_text = requests.get(url=new_url,headers=headers).text
        ex = '<div class="thumb">.*?<img src="(.*?)" alt=.*?</div>'
        ex_data = re.findall(ex,gate_text,re.S)
        for src in ex_data:
            src = 'https:'+src
            img_data = requests.get(url=src,headers=headers).content
            img_name = src.split('/')[-1]
            img_path = './qiushi/' + img_name
            with open(img_path,'wb') as fp:
                fp.write(img_data)
                print(img_name,'success!!')