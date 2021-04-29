import asyncio
import time

async def request(url):
    print('正在请求的url是:',url)
    #在异步协程中如果出现同步模块相关的代码，那么就无法实现异步
    #time.sleep(2)
    await asyncio.sleep(2)
    print('请求成功：',url)
#async修饰的函数，调用之后返回的一个协程对象
start = time.time()
urls = {
    'www.123.com',
    'www.234.com',
    'www.345.com'
}
#存放多个任务对象
stask = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stask.append(task)
loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(stask))

print(time.time()-start)
