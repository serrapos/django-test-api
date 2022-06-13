from django.contrib import admin

from django_test_api.models import Category, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
