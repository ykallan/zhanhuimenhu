# -*- coding: utf-8 -*-

# Scrapy settings for zhanhuimenhu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhanhuimenhu'

SPIDER_MODULES = ['zhanhuimenhu.spiders']
NEWSPIDER_MODULE = 'zhanhuimenhu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'zhanhuimenhu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhanhuimenhu.middlewares.ZhanhuimenhuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'zhanhuimenhu.middlewares.ZhanhuimenhuDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhanhuimenhu.pipelines.ZhanhuimenhuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

proxy_pool = [
    # 'http://221.180.170.104:8080',
    'http://218.60.8.83:3129',
    'http://39.106.223.134:80',

    'http://47.90.97.8:8080',
    'http://183.236.234.44:38070',
    'http://115.231.31.130:80',
    'http://101.37.118.54:8888',
    # 'http://221.180.170.104:8080',
    'http://123.207.17.166:80',
    'http://39.137.69.6:8080',
    'http://183.230.179.164:8060',
    'http://117.59.224.64:80',
    'http://47.104.201.136:55443',
    'http://118.24.182.138:8080',
    'http://119.3.214.196:8080',
    'http://120.79.48.160:8080',
    # 'http://221.180.170.104:8080',
    'http://60.216.20.210:8001',
    'http://223.82.106.253:3128',
    'http://182.32.246.167:9999',
    'http://118.24.88.240:1080',
    'http://221.224.136.211:35101',
    'http://47.104.201.136:55443',
    'http://119.3.214.196:8080',
    'http://211.144.213.145:80',
    'http://182.18.13.149:53281',
    'http://220.168.52.245:40406',
    'http://27.188.65.244:8060',
    'http://111.47.154.34:53281',
    'http://120.236.130.132:8060',
    'http://115.238.59.86:53120',
    # 'http://221.180.170.104:8080',
    'http://183.167.217.152:63000',
    'http://218.22.7.62:53281',
    'http://115.223.7.110:80',
    'http://196.1.184.6:52963',
    'http://167.114.112.84:80',
    'http://200.89.159.153:8080',
    'http://39.106.223.134:80',
    'http://124.232.133.199:3128',
    'http://165.22.55.239:8000',
    'http://159.89.207.165:8888',
    'http://198.98.55.168:8080',
    'http://95.143.8.182:57169',
    'http://138.204.179.162:44088',
    'http://103.46.225.67:8080',
    'http://181.129.183.19:53281',
    'http://124.158.167.170:8080',
    'http://61.19.145.66:8080',
    'http://180.183.25.158:8080',
    'http://46.101.208.13:80',
    'http://213.109.130.184:8080',
    'http://222.223.182.66:8000',
    'http://44.232.52.177:8090',
    'http://116.254.100.165:46675',
    'http://50.192.195.69:52018',
    'http://44.232.52.177:8090',
    'http://92.247.142.14:53281',
    'http://185.188.218.10:60928',
    'http://118.173.233.31:59669',
    'http://202.53.254.34:3128',
    'http://167.71.195.139:8080',
    'http://212.83.180.30:5836',
    'http://91.93.135.113:8080',
    'http://103.233.152.140:8080',
    'http://167.71.195.139:8080',
    'http://177.221.167.62:8080',
    'http://183.88.104.70:8080',
    'http://51.254.237.77:3129',
    'http://178.128.206.2:80',
    'http://181.176.161.19:8080',
    'http://1.196.161.10:9999',
    'http://45.76.87.220:8080',
    'http://118.174.232.237:48665',
    'http://45.127.246.210:8080',
    'http://165.227.71.60:80',
    'http://149.28.130.68:8080',
    'http://105.209.182.128:8080',
    'http://178.219.171.43:45637',
    'http://5.59.145.129:8080',
    'http://98.158.58.200:8080',
    'http://47.88.16.118:3128',
    'http://41.170.84.218:12354',
    'http://47.88.16.118:3128',
    'http://36.92.219.206:30456',
    'http://177.185.157.146:8080',
    'http://36.92.219.206:30456',
    'http://198.12.63.250:58080',
    'http://173.82.55.156:5836',
    'http://103.138.41.74:9999',
    'http://177.94.225.218:8080',
    'http://168.232.20.155:8080',
    'http://92.84.56.10:49556',
    'http://190.152.5.126:53040',
    'http://178.128.28.29:8080',
    'http://131.196.8.1:999',
    'http://83.151.225.191:8080',
    'http://83.151.225.191:8080',
    'http://186.232.48.98:58642',
    'http://128.199.130.51:8080',
    'http://41.223.152.102:8080',
    'http://118.27.13.46:3128',
    'http://62.48.212.126:8080',
    'http://97.92.111.244:443',
    'http://112.133.214.240:80',
    'http://163.172.93.133:5836',
    'http://139.99.222.27:3128',
    'http://170.81.232.241:55302',
    'http://119.82.252.29:34661',
    'http://51.38.71.101:8080',
    'http://103.112.212.133:81',
    'http://173.82.55.157:5836',
    'http://217.150.150.17:80',
    'http://51.158.154.43:5836',
    'http://139.228.61.46:8080',
    'http://190.93.176.70:8080',
    'http://186.229.25.18:8080',
    'http://151.22.181.231:8080',
    'http://45.32.159.125:8080',
    'http://115.127.109.2:45067',
    'http://134.119.179.196:5836',
    'http://187.6.108.42:8080',
    'http://202.166.207.218:56576',
    'http://122.2.28.114:8080',
    'http://45.32.126.175:8080',
    'http://37.59.61.18:8080',
    'http://103.7.129.243:80',
    'http://45.117.74.97:8060',
    'http://190.90.18.179:999',
    'http://125.208.135.146:8080',
    'http://165.22.97.91:8080',
    'http://102.164.202.75:39933',
    'http://110.44.120.144:8080',
    'http://93.183.184.253:8080',
    'http://78.140.7.239:51884',

]
