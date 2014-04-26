from django.db.utils import IntegrityError
from django.test import TestCase
from should_dsl import should

from blog.models.like import Like
from tests.factories.article import ArticleFactory


class LikeComponentTestCase(TestCase):
    def test_should_ensure_uniqueness_of_session_to_article(self):
        article = ArticleFactory.create()
        session_id = 'sandwn0dna0wdnaw09nd0wan'

        Like.objects.create(article=article, session_id=session_id)
        (
            (lambda: Like.objects.create(article=article, session_id=session_id))
            | should | throw(IntegrityError)
        )
