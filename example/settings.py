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
    # 'example.pipelines.JianshuspiderPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 400,

    # 'example.pipelines.SaveImagePipeline': 1,
    # 'example.pipelines.UploadImagePipeline': 2,
    'example.pipelines.SelfDefineFilePipline': 1,
}
DOWNLOADER_MIDDLEWARES = {
    # 'example.middlewares.SeleniumDownloadMiddleware': 543,
    'example.middlewares.SeleniumDownloadMusicMiddleware': 543,
    # 'example.middlewares.MyproxiesSpiderMiddleware': 125,
}
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
MEDIA_ALLOW_REDIRECTS =True
HTTPERROR_ALLOWED_CODES = [301]
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
    "60.167.22.36:9999 ",
    "60.167.21.122:9999 ",
    "125.108.83.110:9000 ",
    "60.167.20.152:9999 ",
    "114.104.139.76:9999 ",
    "59.33.68.218:21990 ",
    "123.55.98.144:9999 ",
    "117.66.254.171:9999 ",
    "112.244.229.55:9000 ",
    "123.133.194.207:47993 ",
    "184.154.222.110:80 ",
    "120.83.120.192:9999 ",
    "106.42.42.227:9999 ",
    "115.221.241.223:9999 ",
    "125.108.89.99:9000 ",
    "221.199.69.191:21120 ",
    "175.43.153.37:9999 ",
    "131.196.143.149:33729 ",
    "125.108.84.13:9000 ",
    "123.149.136.161:9999 ",
    "171.35.171.120:9999 ",
    "58.19.166.15:35186 ",
    "171.35.161.218:9999 ",
    "114.104.184.225:9999 ",
    "42.59.84.55:1133 ",
    "59.62.52.128:9000 ",
    "114.104.143.164:9999 ",
    "123.52.97.144:9999 ",
    "183.149.174.80:41939 ",
    "113.194.22.141:9999 ",
    "106.4.136.140:9000 ",
    "117.66.254.106:9999 ",
    "171.11.29.143:9999 ",
    "183.166.171.216:8888 ",
    "115.221.246.234:9999 ",
    "113.124.84.237:9999 ",
    "171.35.171.106:9999 ",
    "120.83.109.175:9999 ",
    "171.13.136.106:9999 ",
    "125.110.77.227:9000 ",
    "114.101.250.24:26710 ",
    "113.121.41.54:9999 ",
    "171.12.220.107:9999 ",
    "60.167.21.147:9999 ",
    "116.26.39.223:30344 ",
    "39.81.148.238:9000 ",
    "60.167.21.129:9999 ",
    "171.11.179.239:9999 ",
    "113.121.22.40:9999 ",
    "183.166.162.45:9999 ",
    "117.66.254.96:9999 ",
    "113.121.46.72:30870 ",
    "36.248.132.110:9999 ",
    "58.253.154.128:9999 ",
    "183.166.162.252:9999 ",
    "123.54.44.237:9999 ",
    "58.253.157.55:9999 ",
    "110.243.9.22:9999 ",
    "175.42.158.195:9999 ",
    "113.121.93.107:9999 ",
    "113.218.236.33:47584 ",
    "115.221.240.216:9999 ",
    "114.104.142.23:9999 ",
    "58.253.152.178:9999 ",
    "171.11.179.200:9999 ",
    "60.167.21.245:9999 ",
    "58.253.158.227:9999 ",
    "115.210.24.44:9000 ",
    "123.149.39.251:9999 ",
    "123.134.226.11:25238 ",
    "182.34.17.78:9999 ",
    "125.110.119.192:9000 ",
    "117.69.130.181:9999 ",
    "171.35.160.136:9999 ",
    "183.166.139.187:9999 ",
    "123.162.5.150:36823 ",
    "171.35.166.165:9999 ",
    "59.62.25.37:9000 ",
    "125.108.66.217:9000 ",
    "114.106.217.73:46205 ",
    "113.121.42.199:9999 ",
    "115.221.244.202:9999 ",
    "124.112.236.12:3000 ",
    "1.197.204.5:9999 ",
    "175.42.158.3:9999 ",
    "175.42.122.19:9999 ",
    "144.255.49.42:9999 ",
    "183.166.133.222:9999 ",
    "171.35.167.195:9999 ",
    "115.221.241.127:9999 ",
    "123.101.237.45:9999 ",
    "114.223.159.2:53398 ",
    "175.43.59.28:9999 ",
    "218.95.82.205:9000 ",
    "125.108.76.91:9000 ",
    "1.196.105.11:9999 ",
    "114.104.103.135:37945 ",
    "178.62.96.116:80 ",
    "171.35.220.122:9999 ",
    "171.11.179.199:9999 ",
    "113.195.229.169:9999 ",
    "117.63.178.239:9000 ",
    "123.160.68.245:9999 ",
    "113.124.87.187:9999 ",
    "131.196.141.85:33729 ",
    "106.42.216.119:9999 ",
    "171.11.28.127:9999 ",
    "114.99.131.19:1133 ",
    "171.35.163.198:9999 ",
    "113.121.22.139:9999 ",
    "183.3.179.224:28262 ",
    "171.35.171.15:9999 ",
    "115.53.33.89:9999 ",
    "112.111.217.79:9999 ",
    "125.110.80.0:9000 ",
    "123.160.1.253:9999 ",
    "117.64.236.36:1133 ",
    "163.204.94.218:9999 ",
    "180.160.45.30:25639 ",
    "113.195.171.161:9999 ",
    "115.218.209.118:9000 ",
    "115.218.212.172:9000 ",
    "1.198.72.74:9999 ",
    "112.240.176.87:9000 ",
    "58.22.177.143:9999 ",
    "183.166.162.114:9999 ",
    "125.110.120.78:9000 ",
    "183.166.170.105:8888 ",
    "183.166.139.183:9999 ",
    "123.54.40.13:9999 ",
    "218.6.105.145:34097 ",
    "175.44.108.16:9999 ",
    "175.43.33.36:9999 ",
    "114.104.139.63:9999 ",
    "180.118.128.19:9000 ",
    "171.35.168.201:9999 ",
    "1.199.30.109:9999 ",
    "115.221.245.225:9999 ",
    "125.123.153.176:9999 ",
    "27.43.191.128:9999 ",
    "123.54.52.112:9999 ",
    "110.243.18.155:9999 ",
    "171.35.171.183:9999 ",
    "171.35.149.98:9999 ",
    "182.122.178.57:9999 ",
    "59.62.54.5:9000 ",
    "122.241.223.39:36552 ",
    "36.248.133.201:9999 ",
    "91.121.88.53:8010 ",
    "175.44.108.228:9999 ",
    "221.180.170.104:8080",
    "123.207.91.165:1080",
    "39.106.223.134:80",
    "139.155.41.15:8118",
    "183.220.145.3:80",
    "58.220.95.78:9401",
    "113.195.169.147:9999",
    "58.220.95.79:10000",
    "123.163.121.31:9999",
    "124.200.36.118:40188",
    "113.121.95.9:9999",
    "183.154.3.91:9999",
    "101.37.118.54:8888",
    "211.137.52.159:8080",
    "211.137.52.158:8080",
    "113.194.30.189:9999",
    "125.105.146.190:9999",
    "159.226.21.115:80",
    "58.253.159.246:9999",
    "123.101.207.15:9999",
    "120.83.111.63:9999",
    "193.112.113.26:1080",
    "118.24.89.122:1080",
    "110.243.5.159:9999",
    "60.179.230.146:3000",
    "58.220.95.55:9400",
    "171.35.149.172:9999",
    "58.87.68.189:1080",
    "123.207.57.145:1080",
    "124.90.207.169:8118",
    "175.42.68.54:9999",
    "171.35.213.49:9999",
    "113.194.31.246:9999",
    "120.83.107.76:9999",
    "113.121.38.99:9999",
    "110.243.11.168:9999",
    "101.4.136.34:81",
    "140.143.137.69:1080",
    "118.24.128.46:1080",
    "123.55.114.207:9999",
    "27.43.188.107:9999",
    "120.83.104.62:9999",
    "113.124.95.17:9999",
    "118.24.127.144:1080",
    "113.121.22.110:9999",
    "123.207.43.128:1080",
    "139.217.110.76:3128",
    "118.25.13.185:3128",
    "125.90.231.163:8118",
    "59.37.18.243:3128",
    "121.8.146.99:8060",
    "171.35.171.138:9999",
    "113.121.37.89:9999",
    "171.35.215.95:9999",
    "119.29.177.120:1080",
    "140.143.142.200:1080",
    "171.35.173.156:9999",
    "171.35.147.64:9999",
    "123.207.66.220:1080",
    "58.220.95.86:9401",
    "118.24.172.149:1080",
    "223.100.166.3:36945",
    "115.221.240.67:9999",
    "118.24.170.46:1080",
    "120.83.104.215:9999",
    "139.199.153.25:1080",
    "123.207.57.92:1080",
    "112.109.198.105:3128",
    "140.143.142.14:1080",
    "221.122.91.75:10286",
    "140.143.152.93:1080",
    "123.169.102.204:9999",
    "58.220.95.54:9400",
    "58.220.95.90:9401",
    "113.121.21.144:9999",
    "123.169.102.134:9999",
    "123.169.96.93:9999",
    "110.243.3.123:9999",
    "113.195.157.190:9999",
    "115.202.49.155:8118",
    "171.35.163.245:9999",
    "171.35.163.103:9999",
    "112.245.17.202:8080",
    "110.243.12.156:9999",
    "171.35.143.80:9999",
    "58.87.98.150:1080",
    "58.253.159.247:9999",
    "58.220.95.80:9401",
    "171.35.213.211:9999",
    "140.143.156.166:1080",
    "42.238.91.139:9999",
    "171.35.214.0:9999",
    "123.149.137.130:9999",
    "58.250.21.56:3128",
    "183.154.3.2:9999",
    "140.143.142.218:1080",
    "171.35.172.20:9999",
    "58.87.98.112:1080",
]
