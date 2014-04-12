from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views.article import ArticleDetailView
from blog.views.article import ArticleListView
from blog.views.home import HomeView


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',  HomeView.as_view(), name='home'),
    url(r'^articles/(?P<slug>[\w\d\-]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^articles/$', ArticleListView.as_view(), name='article-list'),
)
