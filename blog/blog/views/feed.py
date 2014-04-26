from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models.article import Article


class ArticleFeed(Feed):
    title = 'AndrewCrosio.com Blog Articles'
    link = '/feed/'
    description = 'Updates on changes and additions to AndrewCrosio.com Blog Articles'

    def items(self):
        return Article.objects.order_by('-created_at')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.title

    def item_link(self, item):
        return reverse('article-detail', args=[item.slug])
