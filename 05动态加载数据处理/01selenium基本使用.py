from selenium import webdriver
from lxml import etree
from time import sleep

if __name__ == '__main__':

    bro = webdriver.Chrome(r"E:\google\Chrome\Application\chromedriver.exe")
    bro.get(url='http://scxk.nmpa.gov.cn:81/xk/')

    page_text = bro.page_source
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="gzlist"]/li')
    for li in li_list:
        name = li.xpath('./dl/@title')[0]
        print(name)
    sleep(5)
    bro.quit()