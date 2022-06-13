from .models import Category, Article
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['title']
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['title', content, author, register_date, category]
        fields = '__all__'
