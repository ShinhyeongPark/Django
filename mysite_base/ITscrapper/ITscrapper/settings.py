BOT_NAME = 'ITscrapper'

SPIDER_MODULES = ['ITscrapper.spiders']
NEWSPIDER_MODULE = 'ITscrapper.spiders'

ROBOTSTXT_OBEY = False

FEED_FORMAT = "csv"
FEED_URI = "ITnews.csv"
FEED_EXPORT_ENCODING = 'utf-8-sig'
