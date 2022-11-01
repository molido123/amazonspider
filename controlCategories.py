import time
from threading import Thread

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import finder

# 分别在子页开启chrome，以达到更高效率
# chrome设置
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
chrome_options.add_argument(UserAgent().random)
# 加socks5代理
chrome_options.add_argument("proxy-server=socks5://127.0.0.1:1089")


#
# chrome_options.add_argument('--headless')


# 单个进程对某一种类进行爬取
def entitySearch(category: str, href: str) -> list:
    try:
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(href)
        xPath_All = '//*[@id="gridItemRoot"]'
        # 获取全部元素50

        entities = WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located((By.XPATH, xPath_All)))
        origin0 = entities
        try:
            tmp = entities[29]
            browser.execute_script("arguments[0].scrollIntoView();", tmp)
            time.sleep(8)
            entities = WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located((By.XPATH, xPath_All)))
            origin0 = entities
        except Exception as e:
            print(e)
            entities = origin0
        try:
            tmp = entities[36]
            browser.execute_script("arguments[0].scrollIntoView();", tmp)
            time.sleep(8)
            entities = WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located((By.XPATH, xPath_All)))
            origin0 = entities
        except Exception as e:
            print(e)
            entities = origin0
        try:
            tmp = entities[45]
            browser.execute_script("arguments[0].scrollIntoView();", tmp)
            time.sleep(8)
            entities = WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located((By.XPATH, xPath_All)))
        except Exception as e:
            print(e)
            entities = origin0
        # end
        hrefsOfEntities = []
        namesOfEntities = []
        imagesOfEntities = []
        for entity in entities:
            namesOfEntities.append(entity.text)
            hrefsOfEntities.append(
                str(entity.find_elements(By.XPATH, '//*[@id="gridItemRoot"]//a[2]')[0].get_attribute("href")))
            imagesOfEntities.append(
                entity.find_elements(By.XPATH, '//*[@id="gridItemRoot"]//img')[0].get_attribute("src"))
        if (len(hrefsOfEntities) != len(namesOfEntities) or len(imagesOfEntities) != len(namesOfEntities)) and len(
                imagesOfEntities) != 0:
            print("entitySearch获取的商品信息不符合要求")
            return "error"
    except Exception as e:
        print(e)
        print("entitySearch函数出错")
        return "error"
    print(str(category) + "全部商品的简略信息获取成功")
    # 某一种类的大全
    Entities = []
    count3 = 1
    for i in hrefsOfEntities:
        try:
            Entities.append(finder.findEntity(browser, i, namesOfEntities[count3], imagesOfEntities[count3]))
            count3 = count3 + 1
        except Exception as e:
            print(e)
            print(namesOfEntities[count3] + "获取失败！")
    print(category + "种类获取成功")
    browser.quit()
    # 开始记录在文件中


# 多线程
def controlCategories(categories: list, hrefs: list):
    try:
        count1 = 0
        for href in hrefs:
            Thread(target=entitySearch(categories[count1], href)).run()
            count1 = count1 + 1
    except Exception as e:
        print(e)
        print("controlCategories")
