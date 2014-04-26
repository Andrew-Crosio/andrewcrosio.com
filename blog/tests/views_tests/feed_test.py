from django.test import SimpleTestCase
from django.test import TestCase
from flexmock import flexmock
from should_dsl import should

from blog.views import feed
from tests.factories.article import ArticleFactory


class FeedViewTestCase(SimpleTestCase):
    def setUp(self):
        # Mock out initializer as we don't want to deal with it
        flexmock(feed.ArticleFeed).should_receive('__init__')
        self.view = feed.ArticleFeed()

    def test_article_feed_should_order_by_created_at_and_truncate_to_twenty_items(self):
        queryset_mock = range(100)

        (
            flexmock(feed.Article)
            .should_receive('objects.order_by')
            .with_args('-created_at')
            .and_return(queryset_mock)
            .once()
        )

        self.view.items() | should | equal_to(range(20))

    def test_article_feed_should_get_title_from_item(self):
        title = 'this is the title'
        item_mock = flexmock(title=title)
        self.view.item_title(item_mock) | should | equal_to(title)

    def test_article_feed_should_get_description_from_item(self):
        description = 'this is the description'
        item_mock = flexmock(title=description)
        self.view.item_description(item_mock) | should | equal_to(description)


class FeedViewComponentTestCase(TestCase):
    def setUp(self):
        # Mock out initializer as we don't want to deal with it
        flexmock(feed.ArticleFeed).should_receive('__init__')
        self.view = feed.ArticleFeed()

    def test_article_feed_should_get_link_to_item_detail(self):
        article = ArticleFactory.create(title='test item')
        self.view.item_link(article) | should | equal_to('/articles/test-item/')

