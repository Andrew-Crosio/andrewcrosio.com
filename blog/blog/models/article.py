from django.contrib.auth.models import User
from django.db import models

from blog.models.base import CreatedAtAndUpdatedAtModel
from blog.models.fields import AutoSlugField
from blog.models.fields import Counter


class Article(CreatedAtAndUpdatedAtModel):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(fields=['title'], editable=False)
    author = models.ForeignKey(User, related_name='articles', editable=False)
    content = models.TextField()
    like_count = Counter('likes')

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'blog'
        ordering = ['-id']

    def save(self, *args, **kwargs):
        # TODO: fix this hack
        self.author = User.objects.latest('id')
        return super(Article, self).save(*args, **kwargs)
