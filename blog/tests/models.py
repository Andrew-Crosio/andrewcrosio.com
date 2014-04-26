from django.db import models

from blog.models.base import CreatedAtAndUpdatedAtModel
from blog.models.fields import AutoSlugField
from blog.models.fields import Counter


class MultiFieldSlug(models.Model):
    field_one = models.CharField(max_length=100)
    field_two = models.CharField(max_length=100)
    field_three = models.CharField(max_length=100)
    slug = AutoSlugField(fields=['field_one', 'field_two', 'field_three'])


class DatedModel(CreatedAtAndUpdatedAtModel):
    pass


class CachedCounterModel(models.Model):
    counter = Counter('relation')


class CachedCounterRelation(models.Model):
    other = models.ForeignKey(CachedCounterModel, related_name='relation')
