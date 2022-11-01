from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import finder
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from threading import Thread
from fake_useragent import UserAgent

ua = UserAgent()
for i in range(10):
    # print(ua.random,"\n")
    print(ua.chrome, "\n")
# 分别在子页开启chrome，以达到更高效率
# chrome设置
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument(ua.random)
chrome_options.add_argument('--headless')

# 加socks5代理
chrome_options.add_argument("proxy-server=socks5://127.0.0.1:1089")
browser = webdriver.Chrome(options=chrome_options)
url = "https://www.amazon.com/Amazon-Basics-Non-Slip-Clothes-Hangers/dp/B00FXNAAW2/?th=1"
finder.findEntity(browser, url, "22", "w2w")
# //*[@id="dp-container"]/div[1]/div[1]/div/div