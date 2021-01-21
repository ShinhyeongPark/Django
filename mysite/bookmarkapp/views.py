from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from bookmarkapp.models import Bookmark
from rest_framework.views import APIView
from rest_framework.response import Response


class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

class ApiBookmark(APIView):
    def get(self, request):
        return Response("ok", status=200)