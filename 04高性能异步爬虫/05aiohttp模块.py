import requests,asyncio,time,aiohttp

start = time.time()
urls = [
    'http://127.0.0.1:5000/azb','http://127.0.0.1:5000/xx','http://127.0.0.1:5000/hh'
]

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            #text()返回字符串形式的响应数据
            #read()返回的二进制形式的响应数据
            #json()返回的就是json对象
            #获取响应数据操作之前一定要使用await进行手动挂起

            page_text = await response.text()
            print(page_text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print('总耗时',time.time()-start)


