import asyncio

async def request(url):
    print('正在请求的url是:',url)
    print('请求成功：',url)
#async修饰的函数，调用之后返回的一个协程对象
c = request('www.baidu.com')

# #创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# #将携程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# #task的使用
# loop = asyncio.get_event_loop()
# #基于loop创建一个task对象
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

#future的使用
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
print(task)
loop.run_until_complete(task)
print(task)
