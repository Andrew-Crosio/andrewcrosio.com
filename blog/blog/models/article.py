from django.contrib.auth.models import User
from django.db import models

from blog.models.base import CreatedAtAndUpdatedAtModel
from blog.models.fields import AutoSlugField


class Article(CreatedAtAndUpdatedAtModel):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(fields=['title'], editable=False)
    author = models.ForeignKey(User, related_name='articles', editable=False)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'blog'
        ordering = ['-id']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # TODO: fix this hack
        self.author = User.objects.latest('id')

        return super(Article, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )
