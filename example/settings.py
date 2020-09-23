# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import random
import os

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.JianshuspiderPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,

    # 'example.pipelines.SaveImagePipeline': 1,
    # 'example.pipelines.UploadImagePipeline': 2,
    # 'example.pipelines.SelfDefineFilePipline': 1,
}
DOWNLOADER_MIDDLEWARES = {
    'example.middlewares.SeleniumDownloadMiddleware': 543,
    # 'example.middlewares.SeleniumDownloadMusicMiddleware': 543,
    # 'example.middlewares.MyproxiesSpiderMiddleware': 125,
}
ROBOTSTXT_OBEY = False
# 配置文件的下载路径
# IMAGES_STORE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
IMAGES_STORE = '/Users/caichen/PycharmProjects/spider/jianshu_project/images'
FILES_STORE = '/Users/caichen/PycharmProjects/spider/jianshu_project/music'
LOG_LEVEL = 'DEBUG'
# 连接redis，默认监听127.0.0.1:6379
REDIS_HOST = '127.0.0.1'
# 主机名
REDIS_PORT = 6379
# REDIS_URL = "redis://:caichen123@127.0.0.1:6379"
# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 3
MEDIA_ALLOW_REDIRECTS = True
HTTPERROR_ALLOWED_CODES = [301]
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'close'
}
UA_LIST = ['Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
           'Mozilla/5.0 (compatible; U; ABrowse 0.6;  Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
           'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)',
           'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR   3.5.30729)',
           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0;   Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;   SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)',
           'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1;   .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
           'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
           'Mozilla/4.0 (compatible; Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729); Windows NT 5.1; Trident/4.0)',
           'Mozilla/4.0 (compatible; Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727); Windows NT 5.1; Trident/4.0; Maxthon; .NET CLR 2.0.50727; .NET CLR 1.1.4322; InfoPath.2)',
           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB6; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)']

USER_AGENT = random.choice(UA_LIST)

# settings.py文件下添加mysql的配置信息
MY_SETTINGS = {
    "host": "182.92.97.72",
    "user": "root",
    "passwd": "caichen",
    "db": "webset",
    "port": 3306,
    "charset": "utf8",
    'use_unicode': True,
}

IPPOOL = [
    "103.235.46.154:80",
    "123.125.115.192:80",
    "123.125.115.183:80",
    "123.125.115.165:80",
    "123.125.114.21:80",
    "123.125.114.18:80",
    "123.125.114.107:80",
    "121.8.98.197:80",
    "117.185.17.177:80",
    "117.185.17.17:80",
    "117.185.17.16:80",
    "112.80.255.51:80",
    "112.80.255.77:80",
    "113.214.13.1:1080",
    "114.80.101.26:80",
    "117.185.16.226:80",
    "117.185.16.253:80",
    "117.185.16.31:80",
    "117.185.17.144:80",
    "117.185.17.145:80",
    "117.185.17.151:80",
    "112.80.255.29:80",
    "112.80.248.95:80",
    "111.206.37.161:80",
    "111.206.37.244:80",
    "111.206.37.248:80",
    "111.206.37.68:80",
    "112.80.248.18:80",
    "112.80.248.73:80",
    "112.80.248.75:80",
    "115.223.7.110:80",
    "111.206.37.100:80",
    "59.47.73.57:80",
    "111.13.100.91:80",
    "103.235.46.121:80",
    "3.211.17.212:80",
    "61.135.186.80:80",
    "61.135.186.243:80",
    "61.135.185.176:80",
    "61.135.185.68:80",
    "61.135.185.78:80",
    "61.135.185.160:80",
    "61.135.185.172:80",
    "61.135.185.38:80",
    "61.135.185.156:80",
    "61.135.185.12:80",
    "61.135.185.69:80",
    "61.135.185.152:80",
    "59.120.117.244:80",
    "61.135.185.153:80"
]
