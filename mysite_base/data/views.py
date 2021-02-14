from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView, DayArchiveView, TodayArchiveView
from django.views.generic.edit import FormView
from django import forms
from django.http import HttpResponseRedirect
from .forms import RefreshForm
from django.db.models import Q
from django.shortcuts import render, redirect
#from .forms import RefreshForm
from .models import IT
from .models import SPORTS
from .models import ECO
from .models import ALL
import os

class NewsAll(ListView):
    model = ALL
    
class NewsITLV(ListView):
    model = IT
    form_class = RefreshForm
    template_name = 'it_list.html'
    success_url = '/data/it'
    
    def post(self,request):
        if request.method == "POST":
            form = RefreshForm(request.POST)
            # os.chdir('/Users/etlaou/Downloads/WebProgramming/mysite_base/ITscrapper')
            os.chdir('/mydjango/ITscrapper')
            os.system('scrapy crawl ITscrapper')
            return HttpResponseRedirect('/data/it')
    
class NewsITDV(DetailView):
    model = IT
    
class NewsECOLV(ListView):
    model = ECO
    form_class = RefreshForm
    template_name = 'eco_litst.html'
    success_url = '/data/eco'

    def post(self,request):
        if request.method == "POST":
            form = RefreshForm(request.POST)
            os.chdir('/Users/etlaou/Downloads/WebProgramming/mysite_base/scrapper')
            os.system('scrapy crawl scrapper')
            return HttpResponseRedirect('/data/eco')
    
class NewsECODV(DetailView):
    model = ECO
    
class NewsSPORTSLV(ListView):
    model = SPORTS
    form_class = RefreshForm
    template_name = 'sports_list.html'
    success_url = '/data/sports'

    def post(self,request):
        if request.method == "POST":
            form = RefreshForm(request.POST)
            os.chdir('/Users/etlaou/Downloads/WebProgramming/mysite_base/Sportsscrapper')
            os.system('scrapy crawl Sportsscrapper')
            return HttpResponseRedirect('/data/sports')

class NewsSPORTSDV(DetailView):
    model = SPORTS