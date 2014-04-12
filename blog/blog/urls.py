from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views.article import ArticleView


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 'blog.views.home', name='home'),
    url(r'^articles/(?P<slug>[\w\d\-]+)/', ArticleView.as_view(), name='article-view'),
)
