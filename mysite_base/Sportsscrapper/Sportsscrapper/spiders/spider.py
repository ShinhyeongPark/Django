import scrapy
from Sportsscrapper.items import SportsscrapperItem
from scrapy.http import Request

URL = 'https://www.yna.co.kr/sports/football/%s' #해외축구

start_page = 1

#스포츠 뉴스
class SportsscrapperSpider(scrapy.Spider):
    name = 'Sportsscrapper'
    allowed_domains = ['yna.co.kr']
    start_urls = [URL % start_page]
    
    def start_requests(self):
        for i in range(2): # 0, 1 ~ 9 -> 1 ~ 10
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