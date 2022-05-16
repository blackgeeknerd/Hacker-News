from rest_framework import serializers

from .models import NewsDB


class NewsDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDB
        fields= ('username', 'by', 'news_id', 'score', 'title', 'text', 'url', 'type')