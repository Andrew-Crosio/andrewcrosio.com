from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView


class HomeView(RedirectView):
    url = reverse_lazy('article-list')
