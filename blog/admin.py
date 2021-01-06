from django.contrib import admin
from .models import Category, Article, Trending, Homec, Homel

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Trending)
admin.site.register(Homec)
admin.site.register(Homel)