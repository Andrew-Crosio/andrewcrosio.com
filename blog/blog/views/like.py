import httplib

from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.base import View

from blog.models.article import Article
from blog.models.like import Like


class LikeView(View):
    def get(self, request, slug):
        assert request.session.session_key, 'No session key found!'

        article = get_object_or_404(Article, slug=slug)
        session_id = request.session.session_key

        if Like.objects.filter(article=article, session_id=session_id).exists():
            response = HttpResponse(status=httplib.NOT_MODIFIED)
        else:
            Like.objects.create(article=article, session_id=session_id)

            if request.is_ajax():
                import ipdb;ipdb.set_trace()
                raise NotImplementedError()
            else:
                url = reverse('article-detail', args=[article.slug])
                response = HttpResponseRedirect(url)

        return response
