from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path=r"E:\google\Chrome\Application\chromedriver.exe")

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

bro.switch_to.frame('iframeResult')

div = bro.find_element_by_id('draggable')

#动作链
action = ActionChains(bro)
action.click_and_hold(div)

for i in range(5):
    action.move_by_offset(17,0).perform()
    sleep(0.3)

#释放动作链
action.release()

bro.quit()
