import scrapy

class ScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    writer = scrapy.Field()
    preview = scrapy.Field()
