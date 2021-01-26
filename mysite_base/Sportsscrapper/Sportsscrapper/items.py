import scrapy

class SportsscrapperItem(scrapy.Item):
    title = scrapy.Field()
    #writer = scrapy.Field()
    preview = scrapy.Field()
