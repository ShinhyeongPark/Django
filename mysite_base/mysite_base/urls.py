from django.contrib import admin
from django.urls import path, include
from mysite_base.views import HomeView

#from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('blog/', include('blog.urls', namespace='blog')),
]
