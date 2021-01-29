# Django Web Project

## Blog Web
> 네이버 뉴스 데이터를 크롤링하여 리스트 형식으로 보여주고, 데이터 검색이 가능한 장고 웹 프로젝트  
> 사이트에 존재하는 데이터를 제공하는 Restful API로 설계 및  구현  

## Function
1. News Crawling
	- IT
	- 경제
	- 스포츠
2. Search Keyword
3. Select Post
	- Blog
	- Bookmark
4. REST API

## Directory Tree
```
.
├── ITscrapper
├── Sportsscrapper
├── api
├── blog
├── bookmark
├── data
├── db.sqlite3
├── manage.py
├── mysite_base
├── scrapper
├── static
├── templates
└── venv
```

## Pip List
```
Python 					3.9.1
Djanog(Framework) 		3.1.5
Scrapy 					2.4.1
djangorestframework 	3.12.2
setuptools          	49.2.1
Database				sqlite
```

## How to Run?
```
#가상환경 실행
source venv/bin/activate
#서버 실행
python3 manage.py runserver
```

## API
```
#게시물
http://localhost[PORT]/api/posts

#IT 뉴스
http://localhost[PORT]/api/it

#경제 뉴스
http://localhost[PORT]/api/eco

#스포츠 뉴스
http://localhost[PORT]/api/sports
```

## Screen
### News: Main
![ex_screenshot](./img/main.png)
### News: IT
![ex_screenshot](./img/it.png)
### News: ECO
![ex_screenshot](./img/eco.png)