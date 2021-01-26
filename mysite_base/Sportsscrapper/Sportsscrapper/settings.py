BOT_NAME = 'Sportsscrapper'

SPIDER_MODULES = ['Sportsscrapper.spiders']
NEWSPIDER_MODULE = 'Sportsscrapper.spiders'

ROBOTSTXT_OBEY = False

FEED_FORMAT = "csv"
FEED_URI = "SPOnews.csv"
FEED_EXPORT_ENCODING = 'utf-8-sig'

ITEM_PIPELINES = {
    'Sportsscrapper.pipelines.SportsscrapperPipeline': 100,
}