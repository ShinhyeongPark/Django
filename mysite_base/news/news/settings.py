BOT_NAME = 'news'

SPIDER_MODULES = ['news.spiders']
NEWSPIDER_MODULE = 'news.spiders'

ROBOTSTXT_OBEY = False

FEED_FORMAT = "csv"
FEED_URI = "news.csv"
FEED_EXPORT_ENCODING = 'utf-8-sig'

ITEM_PIPELINES = {
    'news.pipelines.ItscrapperPipeline': 100,
    'news.pipelines.ScrapperPipeline': 100,
    'news.pipelines.SportsscrapperPipeline': 100,
}