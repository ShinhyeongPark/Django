import scrapy
from news.items import SportsscrapperItem #Sports
from scrapy.http import Request

SPORTS_URL = 'https://www.yna.co.kr/sports/football/%s' #해외축구
start_page = 1


def remove_space(descs:list) -> list:
    result = []
    for i in range(len(descs)):
        if len(descs[i].strip()) > 0:
            result.append(descs[i].strip())

    return result

class SportsscrapperSpider(scrapy.Spider):
    name = 'Sportsscrapper'
    allowed_domains = ['yna.co.kr']
    start_urls = [SPORTS_URL % start_page]
    
    def start_requests(self):
        for i in range(4): # 1 ~ 4
            yield Request(url=URL % (i + start_page), callback=self.parse)

    def parse(self, response):
        titles = response.xpath('//*[@id="container"]/div/div/div[1]/section/div[1]/ul/li/div/div[2]/a/strong/text()').extract()
        previews = response.css('.lead::text').extract()
        
        # zip(titles, writers, previews)
        items = []
        # items에 XPATH, CSS를 통해 추출한 데이터를 저장 
        for idx in range(len(titles)):
            item = SportsscrapperItem()
            item['title'] = titles[idx]
            #item['writer'] = writers[idx]
            item['preview'] = previews[idx]

            items.append(item)

        return items