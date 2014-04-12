from django.views.generic.detail import DetailView

from blog.models.article import Article


class ArticleView(DetailView):
    model = Article
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context.update({
            'title': self.object.title,
            'hide_header': True
        })
        return context
