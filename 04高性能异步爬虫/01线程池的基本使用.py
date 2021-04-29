import time
#单线程串行方式执行
start_time = time.time()
def get_page(str):
    print('正在下载：',str)
    time.sleep(2)
    print('下载完成：',str)

name_list = ['haha','lala','duoduo','anan']

for i in range(len(name_list)):
    get_page(name_list[i])

end_time = time.time()
print(end_time-start_time)

# import time
# from multiprocessing.dummy import Pool
# #单线程串行方式执行
# start_time = time.time()
# def get_page(str):
#     print('正在下载：',str)
#     time.sleep(2)
#     print('下载完成：',str)
#
# name_list = ['haha','lala','duoduo','anan']
#
# pool = Pool(4)
# pool.map(get_page,name_list)
#
#
# end_time = time.time()
# print(end_time-start_time)