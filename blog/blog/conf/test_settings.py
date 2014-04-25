from .settings import *


INSTALLED_APPS = INSTALLED_APPS + ('django_nose',)

# Django Nose Test Runner
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
