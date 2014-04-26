from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views.article import ArticleDetailView
from blog.views.article import ArticleListView
from blog.views.feed import ArticleFeed
from blog.views.home import HomeView


urlpatterns = patterns('',
    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # Home Page (redirects to articles list)
    url(r'^$',  HomeView.as_view(), name='home'),

    # Article views
    url(r'^articles/(?P<slug>[\w\d\-]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^articles/$', ArticleListView.as_view(), name='article-list'),

    # Feeds
    url(r'^feed/$', ArticleFeed(), name='feed')
)
