from django.db import models

from blog.models.article import Article


class Like(models.Model):
    article = models.ForeignKey(Article, related_name='likes')
    session_id = models.CharField(max_length=255)

    class Meta:
        unique_together = ['article', 'session_id']
