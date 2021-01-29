from django.urls import path, include
from api.views import PostViewSet, ITViewSet, ECOViewSet, SPORTSViewSet
app_name = 'api'

post_list = PostViewSet.as_view({ 'get':'list' })
post_detail = PostViewSet.as_view({ 'get':'retrieve' })
it_list = ITViewSet.as_view({ 'get':'list' })
it_detail = ITViewSet.as_view({ 'get':'retrieve' })
eco_list = ECOViewSet.as_view({ 'get':'list' })
eco_detail = ECOViewSet.as_view({ 'get':'retrieve' })
sports_list = SPORTSViewSet.as_view({ 'get':'list' })
sports_detail = SPORTSViewSet.as_view({ 'get':'retrieve' })

urlpatterns = [
    #api/posts
    path('posts/', post_list, name='post_list'),
    #api/posts/int
    path('posts/<int:pk>', post_detail, name='post_detail'),
    #api/posts
    path('it/', it_list, name='it_list'),
    #api/posts/int
    path('it/<int:pk>/', it_detail, name='it_detail'),
    #api/posts
    path('eco/', eco_list, name='eco_list'),
    #api/posts/int
    path('eco/<int:pk>/', eco_detail, name='eco_detail'),
    #api/posts
    path('sports/', sports_list, name='sports_list'),
    #api/posts/int
    path('sports/<int:pk>/', sports_detail, name='sports_detail'),
]