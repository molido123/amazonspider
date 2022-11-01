from cmath import e
from tkinter.font import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

opt = Options()
opt.add_experimental_option('excludeSwitches',['enable-automation'])
##opt.add_argument('--headless')
opt.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')
##启动driver
browser=webdriver.Chrome(options=opt)
try:
    browser.get("https://www.amazon.cn/dp/B000F9RAVS/ref=sr_1_3?keywords=%E7%94%B5%E8%84%91&qid=1666974929&sr=8-3")
    time.sleep(10)
    price=browser.find_elements(By.XPATH,"/html/body/div[2]/div[2]/div[6]/div[3]/div[4]/div[11]/div[3]/div[1]/span/span[2]")
    print(price[0].text)
    browser.quit()
except Exception as e:
    print(e)
    browser.quit()