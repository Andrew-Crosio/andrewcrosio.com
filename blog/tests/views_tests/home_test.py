from django.http.response import HttpResponsePermanentRedirect
from django.test import TestCase
from django.test import Client
from should_dsl import should


class HomeViewComponentTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view_should_redirect_to_articles(self):
        response = self.client.get('/')
        response | should | be_kind_of(HttpResponsePermanentRedirect)
        location = dict(response.items())['Location']
        location | should | equal_to('http://testserver/articles/')
