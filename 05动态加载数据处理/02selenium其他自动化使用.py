from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path=r"E:\google\Chrome\Application\chromedriver.exe")

bro.get(url='https://www.taobao.com/')

#标签定位
search_input = bro.find_element_by_id('q')
sleep(2)
#执行一组js代码，使得滚轮向下滑动
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
#标签交互
search_input.send_keys('女装')
button = bro.find_element_by_class_name('btn-search')
button.click()

bro.get('https://www.baidu.com')
sleep(2)
bro.back()
sleep(2)
bro.forward()
sleep(5)
bro.quit()