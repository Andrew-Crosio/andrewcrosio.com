"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.conf.settings")

application = get_wsgi_application()


def main():
    from gevent import monkey
    from gevent.wsgi import WSGIServer

    monkey.patch_all(thread=False)

    server = WSGIServer(('0.0.0.0', 8080), application)

    print 'Starting gevent server on http://0.0.0.0:8080'

    server.serve_forever()


if __name__ == '__main__':
    main()
