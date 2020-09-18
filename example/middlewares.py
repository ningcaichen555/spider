# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from urllib.request import Request

# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
import time
import os
from selenium.webdriver.chrome.options import Options
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json
from .settings import IPPOOL


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        path = os.path.dirname(os.path.abspath(__file__))
        self.driver = webdriver.Chrome(executable_path=path + "/chromedriver", chrome_options=chrome_options)

    def process_request(self, request, spider):
        print(request)
        self.driver.get(request.url)
        time.sleep(0.5)
        try:
            while True:
                # 这里因为有些文章下方有许多加载更多，在文章被一下专栏收录里，所以要重复点击
                showmore = self.browser.find_element_by_class_name('show-more')
                showmore.click()
                time.sleep(1)
                if not showmore:
                    break
        except:
            pass
        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url, body=source, encoding='utf-8', request=request)
        return response


class MyproxiesSpiderMiddleware(object):
    def __init__(self, ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        print("this is ip:" + thisip)
        request.meta["proxy"] = "http://" + thisip

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200:
            proxy = self.get_random_proxy()
            print("this is response ip:" + proxy)
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            return request
        return response

    def get_random_proxy(self):
        '''随机从文件中读取proxy'''
        while 1:
            with open('你保存的\proxies.txt', 'r') as f:
                proxies = f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies).strip()
        return proxy


class SeleniumDownloadMusicMiddleware(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        path = os.path.dirname(os.path.abspath(__file__))
        # self.driver = webdriver.Chrome(executable_path=path + "/chromedriver", chrome_options=chrome_options)
        self.driver = webdriver.Chrome(executable_path=path + "/chromedriver")
        # self.driver.set_window_size(400, 800)  # 分辨率 1024*768
        time.sleep(1)

    def process_request(self, request, spider):
        print("process_request" + str(request))
        if request.meta.get("Middleware") == "Selenium":
            self.driver.get(request.url)
            time.sleep(0.5)
            locator = (By.CLASS_NAME, "aplayer-more")
            downLoad = (By.CLASS_NAME, "aplayer-list-download")
            downLoad_text = (By.CLASS_NAME, "input-group-text")
            list = []
            musicItem = {}
            names = []
            file_urls = []
            page = 0
            try:
                while True:
                    # 这里因为有些文章下方有许多加载更多，在文章被一下专栏收录里，所以要重复点击
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
                    target = self.driver.find_element_by_class_name("aplayer-more")
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    showmore = self.driver.find_element_by_class_name('aplayer-more')
                    if showmore.text == "没有了":
                        downClick = self.driver.find_elements_by_class_name('aplayer-list-download')
                        downName = self.driver.find_elements_by_class_name('aplayer-list-title')
                        top = self.driver.find_element_by_class_name('aplayer-list-light')
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", top)
                        self.driver.execute_script("window.scrollBy(0, -100)")
                        t = 0
                        for downClickItem in downClick:
                            if t == 200:
                                break
                            name = downName[t].text
                            t = t + 1
                            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(downLoad))
                            if downClickItem.is_enabled():
                                try:
                                    downClickItem.click()
                                except Exception as e:
                                    print("点击异常" + str(e))
                                    self.driver.find_element_by_class_name("close").click()
                                    continue

                                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(downLoad_text))
                                target_class = self.driver.find_elements_by_xpath(
                                    '//*[contains(@class,"download") and contains(@class,"btn-outline-secondary") and contains(@class,"btn")]')
                                for class_type in target_class:
                                    href = class_type.get_attribute('href')
                                    match = re.match("http://.*HQ.*", href)
                                    if match:
                                        names.append(name)
                                        file_urls.append(match.group(0))
                                        musicItem["names"] = names
                                        musicItem["file_urls"] = file_urls
                                        self.driver.execute_script("arguments[0].scrollIntoView(true);", downClickItem)
                                        break
                                self.driver.find_element_by_class_name("close").click()
                            else:
                                self.driver.execute_script("arguments[0].scrollIntoView(true);", downClickItem)
                        break
                    else:
                        showmore.click()
                        time.sleep(0.5)
                list.append(musicItem)
            except Exception as e:
                print(e)
            source = json.dumps(list, ensure_ascii=False)
            response = HtmlResponse(url=self.driver.current_url, body=source, encoding='utf-8', request=request)
            return response
