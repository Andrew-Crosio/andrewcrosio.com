from django.test import TestCase
from should_dsl import should

from blog.models import Article
from tests.factories.article import ArticleFactory
from tests.factories.like import LikeFactory
from tests.factories.user import UserFactory


class ArticleComponentTestCase(TestCase):
    def test_slug_field_should_automatically_slugify_title(self):
        user = UserFactory.create()
        article = Article(
            title='This is a title',
            author=user,
            content='Blah blah some content'
        )
        article.save()

        article.slug | should | equal_to('this-is-a-title')

    def test_should_cache_like_relation_count_when_added(self):
        # Create a new article from factory
        article = ArticleFactory.create()
        article.like_count | should | equal_to(0)

        # Now we'll ad some likes to it
        for count in xrange(1, 10):
            LikeFactory.create(article=article)
            article.like_count | should | equal_to(count)

    def test_should_cache_like_relation_count_when_removed(self):
        article = ArticleFactory.create()
        for count in xrange(1, 10):
            LikeFactory.create(article=article)

        for count in xrange(8, -1, -1):
            article.likes.latest('id').delete()
            article.like_count | should | equal_to(count)
