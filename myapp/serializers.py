from rest_framework import serializers
from .models import Article, Classification

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Article
        fields = [
            'id',
            'title',
            'language',
            'classification_id',
            'number',
            'video_url']
        
class ClassificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Classification
        fields = ['id','title', 'created_time']
