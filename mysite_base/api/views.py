from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import PostSerializer
from api.serializers import ITSerializer, ECOSerializer, SPORTSSerializer
from blog.models import Post
from data.models import IT, ECO, SPORTS

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class ITViewSet(viewsets.ModelViewSet):
    queryset = IT.objects.all()
    serializer_class = ITSerializer
    permission_classes = [permissions.IsAuthenticated]

class ECOViewSet(viewsets.ModelViewSet):
    queryset = ECO.objects.all()
    serializer_class = ECOSerializer
    permission_classes = [permissions.IsAuthenticated]

class SPORTSViewSet(viewsets.ModelViewSet):
    queryset = SPORTS.objects.all()
    serializer_class = SPORTSSerializer
    permission_classes = [permissions.IsAuthenticated]