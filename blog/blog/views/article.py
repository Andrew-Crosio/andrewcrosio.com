from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from blog.models.article import Article


class ArticleDetailView(DetailView):
    model = Article
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context.update({
            'title': self.object.title,
            'hide_header': True
        })
        return context


class ArticleListView(ListView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['title'] = 'Articles'
        return context
