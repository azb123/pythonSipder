from urllib.request import Request,urlopen
from urllib.parse import urlencode

def get_html(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    req = Request(url,headers=head)
    info = urlopen(req)
    return info.read()
def save_html(filename,html_bytes):
    with open(filename,'wb') as f:
        f.write(html_bytes)

def main():
    content = input("请输入要下载的内容：")
    size = int(input("请输入要下载的页数："))
    base_url = 'https://tieba.baidu.com/f?ie=utf-8&{}'
    for pn in range(size):
        args = {
            'pn': pn * 50,
            'kw': content
        }
        args = urlencode(args)
        html_bytes = get_html(base_url.format(args))
        print('正在下载第{}页'.format(pn+1))
        filename = '第{}页.html'.format(pn)
        save_html(filename,html_bytes)


if __name__ == '__main__':
    main()