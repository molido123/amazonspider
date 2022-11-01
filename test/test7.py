from fake_useragent import UserAgent
from selenium import webdriver

import finder

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
url = "https://www.amazon.com/HotHands-Hand-Warmers-Odorless-Activated/dp/B0007ZF4OA/ref=zg_bs_sporting-goods_sccl_10/146-4943652-1525447?pd_rd_i=B0007ZF4OA&psc=1"
finder.findEntity(browser, url, "22", "w2w")
browser.quit()
# //*[@id="dp-container"]/div[1]/div[1]/div/div