from .settings import *


INSTALLED_APPS = INSTALLED_APPS + ('django_nose', 'tests',)

# Django Nose Test Runner
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
