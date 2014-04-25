from django.db import models
from django.utils.text import slugify


# TODO: handle slug field conflicts
class AutoSlugField(models.SlugField):
    def __init__(self, fields=None, *args, **kwargs):
        self._fields = fields
        super(AutoSlugField, self).__init__(*args, **kwargs)

    @staticmethod
    def get_value(fields):
        return '-'.join(slugify(unicode(field)) for field in fields)

    def pre_save(self, model_instance, add):
        field_values = [getattr(model_instance, field) for field in self._fields]
        new_value = self.get_value(field_values)
        setattr(model_instance, self.name, new_value)
        return new_value
