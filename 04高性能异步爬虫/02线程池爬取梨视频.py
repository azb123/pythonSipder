import requests,re,random
from lxml import etree
from multiprocessing.dummy import Pool
urls = [] #视频地址和视频名称的字典
#获取视频假地址函数
def get_videoadd(detail_url,video_id):
    ajks_url = 'https://www.pearvideo.com/videoStatus.jsp'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
                      'Referer':detail_url
    }
    params = {
        'contId': video_id,
        'mrd': str(random.random())
    }
    video_json = requests.post(headers=header,url=ajks_url,params=params).json()
    return video_json['videoInfo']['videos']['srcUrl']
#获取视频数据和持久化存储
def get_videoData(dic):
    right_url = dic['url']
    print(dic['name'],'start!')
    video_data = requests.get(url=right_url,headers=headers).content
    with open(dic['name'],'wb') as fp:
        fp.write(video_data)
    print(dic['name'],'over!')


if __name__ == '__main__':
    url = 'https://www.pearvideo.com/category_6'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }

    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
    for li in li_list:
        detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
        #解析视频ID
        video_id = detail_url.split('/')[-1].split('_')[-1]
        false_url = get_videoadd(detail_url,video_id)
        temp = false_url.split('/')[-1].split('-')[0]
        #拼接出正确的url
        right_url = false_url.replace(temp,'cont-'+str(video_id))
        dic = {
            'name':name,
            'url':right_url
        }
        urls.append(dic)
    #使用线程池
    pool = Pool(4)
    pool.map(get_videoData,urls)
    #子线程结束后关闭
    pool.close()
    #主线程关闭
    pool.join()