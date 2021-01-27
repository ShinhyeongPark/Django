import scrapy
from news.items import ItscrapperItem #IT
from scrapy.http import Request

IT_URL = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230&page=%s' #IT일반

start_page = 1

def remove_space(descs:list) -> list:
    result = []
    for i in range(len(descs)):
        if len(descs[i].strip()) > 0:
            result.append(descs[i].strip())

    return result


class ITscrapperSpider(scrapy.Spider):
    name = 'ITscrapper'
    allowed_domains = ['naver.com']
    start_urls = [IT_URL % start_page]
    
    def start_requests(self):
        for i in range(5): # 0, 1 ~ 9 -> 1 ~ 10
            yield Request(url=URL % (i + start_page), callback=self.parse)

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract()
        titles = remove_space(titles)

        writers = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()
        # zip(titles, writers, previews)
        items = []
        # items에 XPATH, CSS를 통해 추출한 데이터를 저장 
        for idx in range(len(titles)):
            item = ItscrapperItem()
            item['title'] = titles[idx]
            item['writer'] = writers[idx]
            item['preview'] = previews[idx]

            items.append(item)

        return items