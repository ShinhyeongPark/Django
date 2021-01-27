import scrapy

# class NewsItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class ScrapperItem(scrapy.Item):
    title = scrapy.Field()
    writer = scrapy.Field()
    preview = scrapy.Field()
    crawled_time = scrapy.Field()

class ItscrapperItem(scrapy.Item):
    title = scrapy.Field()
    writer = scrapy.Field()
    preview = scrapy.Field()
    crawled_time = scrapy.Field()

class SportsscrapperItem(scrapy.Item):
    title = scrapy.Field()
    preview = scrapy.Field()
    crawled_time = scrapy.Field()