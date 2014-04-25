# coding=utf-8
"""User factory"""
from django.contrib.auth.models import User
import factory


class UserFactory(factory.DjangoModelFactory):
    """User factory"""
    FACTORY_FOR = User

    email = factory.Sequence(lambda n: 'testemail%d@test.org' % n)
    username = factory.Sequence(lambda n: 'testuser%d' % n)
    first_name = factory.Sequence(lambda n: 'testuser%d' % n)
    last_name = factory.Sequence(lambda n: 'testuser%d' % n)
    password = factory.PostGenerationMethodCall('set_password', 'test')
    is_active = True
    is_superuser = False
