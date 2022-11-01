from controlCategories import *

# chrome设置
# 伪装设置
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
chrome_options.add_argument(UserAgent().chrome)
# 加socks5代理
# chrome_options.add_argument("proxy-server=socks5://127.0.0.1:1089")
# 是否开启无头
chrome_options.add_argument('--headless')
# 启动driver
browser = webdriver.Chrome(options=chrome_options)
# 针对url="https://www.amazon.com//bestsellers/"
# 获取种类名字总表
# //div[@role="treeitem"]/a
categoryText = []
# 链接总表
# //div[@role="treeitem"]/a/@herf
hrefs = []
try:
    # 主进程，获取商品信息，并且确保names不为空
    count = 0
    while True:
        url = "https://www.amazon.com//bestsellers/"
        browser.get(url)
        Xpath0 = '//div[@role="treeitem"]/a'
        # XPath0 = """//*[@id="search"]//div/h2/a"""这是为了获取商品实体的url的,因需求搞错废弃
        # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div/div/h2/a
        names = WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located((By.XPATH, Xpath0)))
        # 将names的信息提取
        for i in names:
            categoryText.append(i.text)
            hrefs.append(str(i.get_attribute("href")))
        if len(names) * len(hrefs) != 0 and len(names) == len(hrefs):
            break
        ++count
    # 主进程完结分别爬取商品信息
    print("重复" + str(count) + "次")
    print("*" * 50)
    print("已获取到所有种类和链接")
    count_m = 1
    for m in categoryText:
        print(str(count_m) + ". " + m + '\n')
        count_m = count_m + 1
    print('\n')
    while True:
        one = input("\nchoose one\n")
        if one.isdigit():
            break
        print("\nwrong input\n")
    one = int(one) - 1
    print("you choose " + categoryText[int(one)])
    #    with open('result.txt', 'a', encoding='utf-8') as f:
    #        for item in names:
    #            f.write('\n')
    #            f.write(item.text)
    browser.quit()
    # 开始进入不同种类爬取
    # Result = controlCategories(categoryText, hrefs)
    # 修正后单线程版本
    for i in range(1, 3):
        print("\n总栏第" + str(i) + "页\n")
        href = hrefs[int(one)]
        href = href + "/?pg=" + str(i)
        entitySearch(categoryText[int(one)], href)
    print("子页爬取完毕")
    # 子页爬取完毕
    browser.quit()
except Exception as e:
    print(e)
    browser.quit()
