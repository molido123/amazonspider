# 价格的xpath
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Entity import *


# 商品获取
def findEntity(browser, href: str, name: str, image: str) -> Entity:
    time.sleep(1)
    # id_ = re.findall("/dp/([a-z-A-Z-0-9]*)/", href)
    # comments = reviewsFinder(id_[0], browser)
    #
    # Entity要素
    # 商品价格
    price0 = ""
    # 商品名称
    name0 = name
    # 商品简介（about this item）
    brief0 = ""
    # description
    description0 = ""
    # product image
    image0 = image
    # origin form
    country0 = ""
    # product information
    product_information = {}
    # 物品编号
    IDE = re.findall("/dp/([a-z-A-Z-0-9]*)/", href)[0]
    # 评论数量
    ratings = "0"
    #
    #
    # 获取第一页面
    browser.get(href)
    # 预防弹窗
    # browser.refresh()
    # 得到description
    try:
        xpath_description = '//*[@id="productDescription"]'
        description0 = \
            WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located((By.XPATH, xpath_description)))[0].text
    except Exception as e:
        print(e)
        description0 = "not found!"
    # 得到价格
    try:
        time.sleep(4)
        xpath1 = '//*[@id="corePrice_feature_div"]/div/span/span[2]'
        xpath2 = '//*[@id="corePrice_feature_div"]//span'
        xpath3 = '//*[@id="corePrice_feature_div"]/div/span/span[2]'
        a = []
        b = []
        c = []
        try:
            a = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath1)))
        except Exception as e:
            print(e)
            a = []
        try:
            b = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath2)))
        except Exception as e:
            print(e)
            b = []
        try:
            c = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath3)))
        except Exception as e:
            print(e)
            c = []

        if len(a) != 0 and a[0].text != "":
            price0 = a[0].text
        elif len(b) != 0 and b[0].text != "":
            price0 = b[0].text
        elif len(c) != 0 and c[0].text != "":
            price0 = c[0].text
        else:
            price0 = str(re.findall("\n(\$[0-9]*.[0-9]*)", name0)[0])

    except Exception as e:
        print(e)
        print(name0 + "价格获取异常")
    # 得到简介
    try:
        xpath1 = '//*[@id="feature-bullets"]'
        xpath2 = '//*[@id="bookDescription_feature_div"]/div/div[1]'
        a1 = []
        b1 = []
        try:
            a1 = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath1)))
        except Exception as e:
            print(e)
            a1 = []
        try:
            b1 = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath2)))
        except Exception as e:
            print(e)
            b1 = []
        if len(a1) != 0 and a1[0].text != "":
            brief0 = a1[0].text
        elif len(b1) != 0 and b1[0].text != "":
            brief0 = b1[0].text
        else:
            print(name0 + "not found brief")
            brief0 = "Not Found!"
    except Exception as e:
        print(e)
        print(name0 + '简介获取异常')
    # 获取product information
    # 网页结构分为两种
    # 第一种//*[@id="prodDetails"]
    # 一次取完//*[@id="prodDetails"]//tbody/tr[i]（单值）
    # //*[@id="prodDetails"]//tbody 查看有几个tbody 如果多个可能会导致显示不全
    # //*[@id="prodDetails"]//tbody/tr[i]/th取左栏td右
    # 第二种//*[@id="detailBullets_feature_div"]
    # //*[@id="detailBullets_feature_div"]/ul/li/span/span(出双值）
    # //*[@id="detailBullets_feature_div"]/ul/li/span（出单值）
    # //*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[i] 取出左右值
    # i=1时为左，i=2时为右
    try:
        xpath0 = '//*[@id="prodDetails"]//tbody/tr'
        xpath1 = '//*[@id="detailBullets_feature_div"]/ul/li'
        a4 = []
        b4 = []
        try:
            a4 = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath0)))
        except Exception as e:
            print(e)
        try:
            b4 = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath1)))
        except Exception as e:
            print(e)
        if len(a4) != 0:
            for x in a4:
                left = x.find_elements(By.XPATH, './th')[0].text
                right = x.find_elements(By.XPATH, './td')[0].text
                product_information[left] = right
        elif len(b4) != 0:
            for y in b4:
                left = y.find_elements(By.XPATH, './span/span[1]')[0].text
                right = y.find_elements(By.XPATH, './span/span[2]')[0].text
                product_information[left] = right
    except Exception as e:
        print(e)
        print(name0 + "商品参数检测异常")
    # 设置国家
    try:
        country0 = product_information.get('Country of Origin :')
        if country0 is None:
            country0 = product_information.get('Country of Origin')
    except Exception as e:
        print(e)
        country0 = "国家不明"
    # 获取评论数
    # //div[@data-hook="total-review-count"] 评论数量 在评论总页面
    ratings_url = "https://www.amazon.com//product-reviews/"
    ratings_url = ratings_url + IDE
    browser.get(ratings_url)
    xpath_ratings = '//div[@data-hook="total-review-count"]'
    try:
        ratings = WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath_ratings)))[
            0].text
    except Exception as e:
        print(e)
        print(name0 + "评论数量获取异常")
    result = Entity(name0.split('\n')[0] + " " + name0.split('\n')[1], image0, price0.replace('\n', '.'), brief0,
                    description0, country0, product_information, IDE, ratings)

    return result


# 评论获取
# https://www.amazon.com//product-reviews/[商品编号]
# //*[@id="cm_cr-review_list"]//a/div/span 名字
# //*[@id="cm_cr-review_list"]//div/a/i/span 评分
# //*[@id="cm_cr-review_list"]//span[@data-hook]/span ##评论
# raw+?pageNumber=3 # 换页

# 查找评论暂时废弃
@DeprecationWarning
def reviewsFinder(id_, browser):
    raw = "https://www.amazon.com//product-reviews/"
    count = 1
    remarks = []
    while True:
        try:
            url = raw + id_ + "?pageNumber=" + str(count)
            browser.get(url)
            time.sleep(5)
            # 先获取根结点元素
            all_ = browser.find_elements(By.XPATH, """//*[@id="cm_cr-review_list"]/div""")
            if len(all_) == 0:
                break
            for i in all_:
                tmp = Review("0", "0", "0")
                tmp_name = i.find_elements(By.XPATH, """//a/div/span""")
                if len(tmp_name) == 0:
                    continue
                tmp_name = tmp_name[0].text
                tmp_star = i.find_elements(By.XPATH, """//div/a/i/span""")[0].text
                tmp_content = i.find_elements(By.XPATH, """//span[@data-hook]/span""")
                tmp.name = tmp_name
                tmp.star = tmp_star
                tmp.content = tmp_content
                remarks.append(tmp)
            count = count + 1
        except Exception as e:
            print(e)
            remarks.append(Review("0", "0", "0"))
    return remarks
