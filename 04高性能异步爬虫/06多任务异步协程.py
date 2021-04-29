import requests,asyncio,time

start = time.time()
urls = [
    'http://127.0.0.1:5000/azb','http://127.0.0.1:5000/xx','http://127.0.0.1:5000/hh'
]

async def get_page(url):
    print('正在下载',url)
    #request是基于同步，必须使用基于异步的网络请求模块
    response = requests.get(url=url)
    print('下载成功！',url)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('总耗时',time.time()-start)