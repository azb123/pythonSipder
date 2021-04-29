import requests
import re
import base64
#创建sesson对象 保持会话一至
sesson = requests.session()
#请求的url
Sy_url = 'https://kyfw.12306.cn/passport/web/login'
Xq_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64'
Yz_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
#构造请求头
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
#构造请求表单
Xq_parmas = {
    "login_site": "E",
    "module": "login",
    "rand": "sjrand",
    "1555036551227":"",
    "callback": "jQuery19108754385247664451_1555036549517",
    "_": "1555036549518",
}
#对图片页发送请求
response = sesson.get(url=Xq_url,params=Xq_parmas,headers=headers).text
#获取图片数据
image_bs64 = re.findall('"image":"(.*?)",',response)[0]
#解码数据
image = base64.b64decode(image_bs64)
#保存图片
with open('Yz_image.jpg','wb') as f:
    f.write(image)
#构建像素表单
coord_data = {
    "1":"40,40",
    "2":"120,40",
    "3":"180,40",
    "4":"250,40",
    "5":"40,100",
    "6":"120,100",
    "7":"180,100",
    "8":"250,100",}
answerlist = []
input_answer = input('位置：')
#对输入的数字进行切割
answer_list = input_answer.split(' ')
#循环输入的值取出字典相应的坐标
for i in answer_list:
    answerlist.append(coord_data.get(i))
print('answer：' + ','.join(answerlist))
answer = ','.join(answerlist)
#构造data表单
formdata = {
    "username": '1234',
    "password": '1233333',
    "appid": "otn",
    "answer": answer,
}

Yz_parmas = {
    "callback": "jQuery19108754385247664451_1555036549517",
    "answer": answer,
    "rand": "sjrand",
    "login_site": "E",
    "_": "1555036549519",
}

#发送图片验证请求
response_new = sesson.get(url=Yz_url,params=Yz_parmas,headers=headers).text
#获得图片验证信息
print(re.findall('"result_message":"(.*?)"',response_new))
#增加cookies
sesson.cookies.update({
    'RAIL_EXPIRATION':'1555310364529',
    'RAIL_DEVICEID':'K71MCVMaU_fg6Lr5kLs9K5-HrmV-F-LdSuahWpFSW60X8GmWMZiS06V7InVpguAyYJOmW3cNWKx8Giau-aCZEqehQzwLYRMwjHxr1v1EkKjGTn_iX87fpiWNuGK_jPgg-1PgNgIpFMHeEEfDmXfwdmXX2nGNCcuC',
    'route':'495c805987d0f5c8c84b14f60212447d',
})
response = sesson.post(Sy_url,data=formdata)
response.encoding = 'utf-8'
print(re.findall('"result_message":"(.*?)"',response.text))
