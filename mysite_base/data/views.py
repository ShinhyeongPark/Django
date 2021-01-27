from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView
from django.views.generic.dates import MonthArchiveView, DayArchiveView, TodayArchiveView
from django.views.generic.edit import FormView

from django.db.models import Q
from django.shortcuts import render

from .models import IT
from .models import SPORTS
from .models import ECO

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

    
