from django.db import models

from blog.models.base import CreatedAtAndUpdatedAtModel
from blog.models.fields import AutoSlugField


class MultiFieldSlug(models.Model):
    field_one = models.CharField(max_length=100)
    field_two = models.CharField(max_length=100)
    field_three = models.CharField(max_length=100)
    slug = AutoSlugField(fields=['field_one', 'field_two', 'field_three'])


class DatedModel(CreatedAtAndUpdatedAtModel):
    pass
