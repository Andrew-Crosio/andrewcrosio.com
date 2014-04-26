from django.contrib import admin

from blog.models.article import Article
from blog.models.like import Like


admin.site.register(Article)
admin.site.register(Like)
