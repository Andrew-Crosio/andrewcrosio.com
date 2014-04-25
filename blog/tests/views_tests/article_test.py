from django.test import SimpleTestCase
from flexmock import flexmock
from should_dsl import should

from blog.views import article


class ArticleDetailViewTestCase(SimpleTestCase):
    def setUp(self):
        # Mock out initializer as we don't want to deal with it
        flexmock(article.ArticleDetailView).should_receive('__init__')
        self.view = article.ArticleDetailView()

    def test_get_context_data_should_add_object_title_and_header_to_context(self):
        # Mock the view object
        self.view.object = flexmock(title='This is the title')

        # Run the tested function
        context = self.view.get_context_data()

        # Assert everything's fine
        context['hide_header'] | should | be(True)
        context['title'] | should | equal_to(self.view.object.title)


class ArticleListViewTestCase(SimpleTestCase):
    def setUp(self):
        # Mock out initializer as we don't want to deal with it
        flexmock(article.ArticleListView).should_receive('__init__')
        self.view = article.ArticleListView()

    def test_get_context_data_should_add_object_title_and_header_to_context(self):
        # Mock the view object
        self.view.object = flexmock(title='This is the title')
        self.view.object_list = object()  # Needed to pass

        # Run the tested function
        context = self.view.get_context_data()

        # Assert everything's fine
        context['title'] | should | equal_to('Articles')
