BOT_NAME = 'scrapper'

SPIDER_MODULES = ['scrapper.spiders']
NEWSPIDER_MODULE = 'scrapper.spiders'

# Obey robots.txt rules
#원래는 True
ROBOTSTXT_OBEY = False

FEED_FORMAT = "csv"
FEED_URI = "ECOnews.csv"
FEED_EXPORT_ENCODING = 'utf-8-sig'

#ITEM_PIPELINES = {
#    'myscaper.pipelines.MyscaperPipeline': 300,
#}