import scrapy

class SportsscrapperItem(scrapy.Item):
    title = scrapy.Field()
    #writer = scrapy.Field()
    preview = scrapy.Field()
    crawled_time = scrapy.Field()
