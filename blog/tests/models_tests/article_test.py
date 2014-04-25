from django.test import TestCase
from should_dsl import should

from blog.models import Article
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
