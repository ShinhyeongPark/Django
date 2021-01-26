import sqlite3
import datetime
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter


class ItscrapperPipeline:
    # 초기화 메소드
    def __init__(self):
        # DB 설정(자동 커밋)
        # isolation_level=None => Auto Commit
        self.conn = sqlite3.connect('/Users/etlaou/Downloads/WebProgramming/mysite_base/news.db', isolation_level=None)

        # DB 연결
        self.c = self.conn.cursor()

    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('NewsSpider Pipeline Started.')
        self.c.execute("CREATE TABLE IF NOT EXISTS IT_NEWS(id INTEGER PRIMARY KEY AUTOINCREMENT, title text, preview text, writer text, crawled_time text)")

    # Item 건수 별 실행
    def process_item(self, item, spider):
        if not item.get('title') is None:
            # 삽입 시간
            crawled_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 크롤링 시간 필드 추가
            item['crawled_time'] = crawled_time

            # 데이터 -> DB 삽입
            # tuple(item[k] for k in item.keys()) 로 대신해도 된다.
            self.c.execute('INSERT INTO IT_NEWS(title,preview,writer,crawled_time) VALUES(?, ?, ?, ?);', (item.get('title'), item.get('preview'), item.get('writer'), item.get('crawled_time'))) # tuple(item[k] for k in item.keys())

            # 로그
            spider.logger.info('Item to DB inserted.')

            # 결과 리턴
            return item
        else:
            raise DropItem('Dropped Item. Because This Contents is Empty.')

    # 마지막 1회 실행
    def close_spider(self, spider):
        spider.logger.info('NewsSpider Pipeline Stopped.')

        # commit(auto commit으로 설정했지만 혹시 모르니)
        self.conn.commit()

        # 연결 해제
        self.conn.close()

