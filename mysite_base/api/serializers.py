from rest_framework import serializers
from blog.models import Post
from data.models import IT, ECO, SPORTS

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
                'id', 
                'title', 
                'slug',
                'description',
                'content',
                'create_date',
                'modify_date'
                ]

class ITSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT
        fields = ['id','title', 'preview', 'crawled_time']
        
class ECOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECO
        fields = ['id','title', 'preview', 'crawled_time']

class SPORTSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPORTS
        fields = ['id','title', 'preview', 'crawled_time']