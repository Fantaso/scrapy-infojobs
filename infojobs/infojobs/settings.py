import pathlib
from datetime import datetime

BASE = '/home/carlos/github/scrapy_infojobs'

BOT_NAME = 'infojobs'

SPIDER_MODULES = ['infojobs.spiders']
NEWSPIDER_MODULE = 'infojobs.spiders'

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"

ROBOTSTXT_OBEY = False

COOKIES_ENABLED = True
COOKIES_DEBUG = True

#######################
###  AUTO THROTTLE  ###
#######################
DOWNLOAD_DELAY = 2
# CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
# - The dynamic delay calculated will never:
#       go less than DOWNLOAD_DELAY
#       or more than AUTOTHROTTLE_MAX_DELAY
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

################################################
### GENERAL SETTINGS FOR  LOGGING AND FEEDS  ###
################################################
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
FILENAME_PATTERN = datetime.now().strftime(DATETIME_FORMAT)

LOG_PATH = f'{BASE}/logs/{FILENAME_PATTERN}.txt'
FEEDS_CSV_PATH = f'{BASE}/feeds/csv/{FILENAME_PATTERN}.csv'
FEEDS_JSON_PATH = f'{BASE}/feeds/json/{FILENAME_PATTERN}.json'
FEEDS_XML_PATH = f'{BASE}/feeds/xml/{FILENAME_PATTERN}.xml'
IMAGES_PATH = f'{BASE}/media/'

# FEED_EXPORT_FIELDS = [
# fields used to populate the files generated (csv, json, etc).
#   Fields are populated in the order specified here.

# ]

###  LOGGING  ###
LOG_ENABLED = True  # this True only and it will display in stdout
LOG_TO_FILE = False  # if True: writes to logfile. if False: writes to stdout
if LOG_TO_FILE:
    LOG_FILE = LOG_PATH
    LOG_ENCODING = 'utf-8'
    LOG_LEVEL = 'DEBUG'
    LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
    LOG_DATEFORMAT = DATETIME_FORMAT
    # If True, all stdout & stderr of your process will be redirected to the log.
    # example: if you print('hello') it will appear in the scrapy log.
    LOG_STDOUT = True  # default
    # If True, the logs will just contain the root path.
    # If False, it displays the component responsible for the log output.
    # LOG_SHORT_NAMES = False

###  FEEDS  ###
FEED_STORE_EMPTY = True
FEEDS = {
    pathlib.Path(FEEDS_CSV_PATH): {
        'format': 'csv',
        'encoding': 'utf-8',
    },
    FEEDS_JSON_PATH: {
        'format': 'json',
        'encoding': 'utf-8',
        'indent': 4,
    },
    FEEDS_XML_PATH: {
        'format': 'xml',
        'encoding': 'latin1',
        'indent': 8,
    },
}

FEED_STORAGES_BASE = {
    '': 'scrapy.extensions.feedexport.FileFeedStorage',
    'file': 'scrapy.extensions.feedexport.FileFeedStorage',
    'stdout': 'scrapy.extensions.feedexport.StdoutFeedStorage',
    's3': 'scrapy.extensions.feedexport.S3FeedStorage',
    'ftp': 'scrapy.extensions.feedexport.FTPFeedStorage',
}

FEED_EXPORTERS_BASE = {
    'json': 'scrapy.exporters.JsonItemExporter',
    'jsonlines': 'scrapy.exporters.JsonLinesItemExporter',
    'jl': 'scrapy.exporters.JsonLinesItemExporter',
    'csv': 'scrapy.exporters.CsvItemExporter',
    'xml': 'scrapy.exporters.XmlItemExporter',
    'marshal': 'scrapy.exporters.MarshalItemExporter',
    'pickle': 'scrapy.exporters.PickleItemExporter',
}

########################
###  Media & Images  ###
########################
# DOWNLOAD_TIMEOUT = 30
# if implementing more pipelines for specific spiders
#   consider moving config values into the spider itself
IMAGES_STORE = IMAGES_PATH
# ITEM_PIPELINES = {
#     'infojobs.pipelines.TradefestImagesPipeline': 2,
# }

###  SKIP IMAGES  ###
# filter out images smaller than the minimum here stated
# IMAGES_MIN_HEIGHT = 110
# IMAGES_MIN_WIDTH = 110

# IMAGES_EXPIRES = 5  # days
MEDIA_ALLOW_REDIRECTS = True

###  THUMBNAILS  ###
# IMAGES_THUMBS = {
#     'small': (50, 50),
#     'medium': (68, 68),
# }

###  SCRAPY SELENIUM  ###
# from shutil import which
#
# SELENIUM_DRIVER_NAME = 'firefox'
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
# SELENIUM_DRIVER_ARGUMENTS=['-headless']  # '--headless' if using chrome instead of firefox
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_selenium.SeleniumMiddleware': 800
# }


# pip install scrapy-random-useragent
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     'random_useragent.RandomUserAgentMiddleware': 400
# }

SPIDER_MIDDLEWARES_BASE = {
    # Engine side
    # NOTE: replacing the HttpErrorMiddleware to allow 405 status to handle captcha
    'infojobs.middlewares.CustomHttpErrorMiddleware': 50,
    # 'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
    'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
    # Spider side
}

# USER_AGENT_LIST = f"{BASE}/user_agents.txt"
