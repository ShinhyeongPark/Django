from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView, DayArchiveView, TodayArchiveView
from django.views.generic.edit import FormView
from django import forms

from django.db.models import Q
from django.shortcuts import render, redirect
#from .forms import RefreshForm
from .models import IT
from .models import SPORTS
from .models import ECO
import os

class NewsITLV(ListView):
    model = IT

class NewsITDV(DetailView):
    model = IT
    
class NewsECOLV(ListView):
    model = ECO

class NewsECODV(DetailView):
    model = ECO
    

class NewsSPORTSLV(ListView):
    model = SPORTS

class NewsSPORTSDV(DetailView):
    model = SPORTS

class UpdateIT(FormView):
    template_name = "data/it_list.html"
    success_url = "data/it_list.html"

    def form_valid(self, form):
        os.chdir('/Users/etlaou/Downloads/WebProgramming/mysite_base/ITscrapper')
        os.system('scrapy crawl ITscrapper')
        return super().form_valid(form)


class UpdateSPORTS(FormView):
    template_name = "data/sports_list.html"
    success_url = "data/sports_list.html"

    def form_valid(self, form):
        os.chdir('/Users/etlaou/Downloads/WebProgramming/mysite_base/Sportsscrapper')
        os.system('scrapy crawl Sportsscrapper')
        return super().form_valid(form)


class UpdateECO(FormView):
    template_name = "data/eco_list.html"
    success_url = "data/eco_list.html"

    def form_valid(self, form):
        os.chdir('/Users/etlaou/Downloads/WebProgramming/mysite_base/scrapper')
        os.system('scrapy crawl scrapper')
        return super().form_valid(form)