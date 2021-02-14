FROM python:3.7.9-stretch

#COPY할 디렉토리
WORKDIR /mydjango 
#라이브러리를 우선적으로 설치
RUN pip install django
RUN pip install mysqlclient
RUN pip install djangorestframework
RUN pip install scrapy

COPY api /mydjango/api
COPY blog /mydjango/blog
COPY bookmark /mydjango/bookmark
COPY data /mydjango/data
COPY ITscrapper /mydjango/ITscrapper
COPY mysite_base /mydjango/mysite_base
COPY scrapper /mydjango/scrapper
COPY Sportsscrapper /mydjango/Sportsscrapper
COPY templates /mydjango/templates
COPY static /mydjango/static
COPY db.sqlite3 /mydjango/db.sqlite3
COPY manage.py /mydjango/manage.py

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]