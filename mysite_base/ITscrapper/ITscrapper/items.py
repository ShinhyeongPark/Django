import scrapy

class ItscrapperItem(scrapy.Item):
    title = scrapy.Field()
    writer = scrapy.Field()
    preview = scrapy.Field()
