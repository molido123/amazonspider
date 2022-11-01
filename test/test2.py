from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/67.0.3396.99 Safari/537.36')
# 加socks5代理
chrome_options.add_argument("proxy-server=socks5://127.0.0.1:1089")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://whoer.net/zh")
time.sleep(10)
driver.quit()
