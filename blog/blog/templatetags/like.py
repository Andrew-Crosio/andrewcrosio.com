from django import template

register = template.Library()


@register.filter
def has_liked(article, request):
    try:
        session_id = request.session.session_key
    except AttributeError:
        return True

    # TODO: cache this somewhere (perhaps session)
    return article.likes.filter(session_id=session_id).exists()
