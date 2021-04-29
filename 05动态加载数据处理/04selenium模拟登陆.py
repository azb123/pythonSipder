from selenium import webdriver
from time import sleep


bro = webdriver.Chrome(executable_path=r"E:\google\Chrome\Application\chromedriver.exe")
bro.get('https://qzone.qq.com/')
bro.switch_to.frame("login_frame")

switcher = bro.find_element_by_id('switcher_plogin')
switcher.click()

user_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
user_tag.send_keys('1234455')
password_tag.send_keys('qwer123')
sleep(1)

but = bro.find_element_by_id('login_button')
but.click()
