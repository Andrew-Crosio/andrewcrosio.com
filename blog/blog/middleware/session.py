from django.conf import settings
from django.contrib.sessions.middleware import SessionMiddleware


class UbiquitousSessionMiddleware(SessionMiddleware):
    def process_response(self, request, response):
        # If the session id is not yet in the browser's cookies and it won't be put in
        # this request, force it in by modifying the session
        if settings.SESSION_COOKIE_NAME not in request.COOKIES and not request.session.modified:
            request.session.save()
            request.session.modified = True

        return super(UbiquitousSessionMiddleware, self).process_response(request, response)
