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


class Counter(models.IntegerField):
    def __init__(self, getter=None, *args, **kwargs):
        self._getter = getter
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', 0)
        super(Counter, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = self._getter(model_instance)
        setattr(model_instance, self.name, value)
        return value
