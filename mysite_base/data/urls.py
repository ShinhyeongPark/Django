from django.urls import path
from django.conf.urls import url

from data.views import NewsSPORTSLV, NewsITLV, NewsECOLV
from data.views import NewsSPORTSDV, NewsITDV, NewsECODV

app_name = 'data'

urlpatterns = [
    #data/
    path('', NewsITLV.as_view(), name='index'),
    #data/it
    path('it/', NewsITLV.as_view(), name='it_list'),
    #data/eco
    path('eco/', NewsECOLV.as_view(), name='eco_list'),
    #data/sprots
    path('sports/', NewsSPORTSLV.as_view(), name='sports_list'),
    #data/it/숫자
    path('it/<int:pk>/', NewsITDV.as_view(), name='it_detail'),
    #data/eco/숫자
    path('eco/<int:pk>/', NewsECODV.as_view(), name='eco_detail'),
    #data/sports/숫자
    path('sports/<int:pk>/', NewsSPORTSDV.as_view(), name='sports_detail'),
]