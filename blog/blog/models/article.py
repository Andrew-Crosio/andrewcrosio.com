from django.contrib.auth.models import User
from django.db import models

from blog.models.base import CreatedAtAndUpdatedAtModel


class Article(CreatedAtAndUpdatedAtModel):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, related_name='articles')
    content = models.TextField()

    class Meta:
        app_label = 'blog'
