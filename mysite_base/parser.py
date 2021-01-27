# parser.py
import os
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite_base.settings")
django.setup()

from data.models import IT_DATA
# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# URL = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230&page=%s' #IT일반
# start_page = 1
# start_urls = [URL % start_page]

def parse_it():
    # for i in range(5):
        # req = requests.get(url=URL % (i + start_page))
    req = requests.get('https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid2=230&sid1=105&date=20210126&page=1/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    my_titles = soup.select(
        '#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt:nth-child(2) > a'
        )
    data = {}
    for title in my_titles:
        data[title.text] = title.get('href')
    return data

# if __name__=='__main__':
#     it_data_dict = parse_it()
#     for t, l in it_data_dict.items():
#         IT_DATA(title=t, link=l).save()
##main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a
##main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(2) > dl > dt:nth-child(2) > a