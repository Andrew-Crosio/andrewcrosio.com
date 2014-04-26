import httplib

from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.test import TestCase
from django.test import Client
from should_dsl import should

from blog.models.article import Article
from tests.factories.article import ArticleFactory


class LikeViewComponentTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Set up the environment, and make sure a session has been started
        self.client.get('/', follow=True)
    
    def test_user_hitting_like_view_should_increase_like_count(self):
        article = ArticleFactory.create()
        url = reverse('like-article', args=[article.slug])
        article.like_count | should | equal_to(0)

        response = self.client.get(url)

        article_detail_url = reverse('article-detail', args=[article.slug])
        response | should | be_kind_of(HttpResponseRedirect)
        (
            dict(response.items())['Location']
            | should | equal_to('http://testserver' + article_detail_url)
        )

        article = Article.objects.get(pk=article.pk)
        article.like_count | should | equal_to(1)

    def test_user_hitting_like_view_multiples_times_should_increase_like_only_once(self):
        article = ArticleFactory.create()
        url = reverse('like-article', args=[article.slug])
        self.client.get(url)
        article = Article.objects.get(pk=article.pk)
        article.like_count | should | equal_to(1)

        response = self.client.get(url)

        response.status_code | should | equal_to(httplib.NOT_MODIFIED)
        article = Article.objects.get(pk=article.pk)
        article.like_count | should | equal_to(1)

    def test_user_hitting_like_view_for_different_articles_should_increase_on_both(self):
        article_one = ArticleFactory.create()
        article_two = ArticleFactory.create()

        url_one = reverse('like-article', args=[article_one.slug])
        url_two = reverse('like-article', args=[article_two.slug])

        self.client.get(url_one)
        self.client.get(url_two)

        article_one = Article.objects.get(pk=article_one.pk)
        article_two = Article.objects.get(pk=article_two.pk)

        article_one.like_count | should | equal_to(1)
        article_two.like_count | should | equal_to(1)
