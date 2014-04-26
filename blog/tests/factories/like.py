# coding=utf-8
"""Like factory"""
import factory

from blog.models.like import Like
from tests.factories.article import ArticleFactory


class LikeFactory(factory.DjangoModelFactory):
    """Like factory"""
    FACTORY_FOR = Like

    article = factory.SubFactory(ArticleFactory)
    session_id = factory.Sequence(lambda n: 'session_id%d' % n)
