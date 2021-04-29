import requests
import json
if __name__ == '__main__':

    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
    all_data_list = []
    id_list = []  # 储存企业id
    for page in range(1,10):
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname': '',
        }

        json_id = requests.post(url=url,headers=headers,data=data).json()
        for id in json_id['list']:
            id_list.append(id['ID'])

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        detail_data = {
            'id':id
        }
        detail_json = requests.post(url=post_url,data=detail_data,headers=headers).json()
        all_data_list.append(detail_json)
fp = open('./药监总局数据.txt', 'w', encoding='utf-8')
json.dump(all_data_list, fp=fp, ensure_ascii=False)
print('Over!!!')