# -*- coding: utf-8 -*-

# Scrapy settings for Bosszp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Bosszp'

SPIDER_MODULES = ['Bosszp.spiders']
NEWSPIDER_MODULE = 'Bosszp.spiders'

MAX_PAGE = 8

KEYWORDS = ['python爬虫']

MONGO_URI = 'localhost'

MONGO_DB = 'BosszpJobs'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Bosszp (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': ' application/json, text/javascript, */*; q=0.01',
    'accept-encoding': ' gzip, deflate, br',
    'accept-language': ' zh-CN,zh;q=0.9',
    'cache-control': ' no-cache',
    'cookie': ' sid=sem_pz_bdpc_dasou_title; JSESSIONID=""; __g=sem_pz_bdpc_dasou_title; __c=1538176958; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1538176912,1538262027; __l=r=https%3A%2F%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3Dpython%25E7%2588%25AC%25E8%2599%25AB%26scity%3D101280100%26industry%3D%26position%3D&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; lastCity=100010000; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fc100010000%2Fh_100010000%2F%3Fquery%3Dpython%25E7%2588%25AC%25E8%2599%25AB; __a=91863632.1538176911.1538176911.1538176958.46.2.45.46; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1538625561',
    'pragma': ' no-cache',
    'referer': ' https://www.zhipin.com/c100010000/h_100010000/?query=python%E7%88%AC%E8%99%AB',
    'user-agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'x-requested-with': ' XMLHttpRequest',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Bosszp.middlewares.BosszpSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'Bosszp.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Bosszp.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
