# coding=utf-8
"""Article factory"""
import factory

from blog.models.article import Article
from tests.factories.user import UserFactory


class ArticleFactory(factory.DjangoModelFactory):
    """Article factory"""
    FACTORY_FOR = Article

    title = factory.Sequence(lambda n: 'title%d' % n)
    content = factory.Sequence(lambda n: 'content%d' % n)
    author = factory.SubFactory(UserFactory)
