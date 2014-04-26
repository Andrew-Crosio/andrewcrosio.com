from django.db import models
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
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
    def __init__(self, relation=None, *args, **kwargs):
        self._relation = relation

        post_save.connect(self._update_hook)
        post_delete.connect(self._update_hook)

        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', 0)
        super(Counter, self).__init__(*args, **kwargs)

    @property
    def related_field(self):
        try:
            return getattr(self.model, self._relation)
        except (TypeError, AttributeError):
            # When the app has not loaded, just return none, as we don't need to worry
            return None

    @property
    def related_klass(self):
        if self.related_field:
            return self.related_field.related.model
        else:
            return None

    def get_relation(self, instance):
        if self.related_field:
            field_name = self.related_field.related.field.name
            return getattr(instance, field_name)
        else:
            return None

    def _update_hook(self, sender, instance, *args, **kwargs):
        klass = self.related_klass
        if klass and isinstance(instance, self.related_klass):
            relation = self.get_relation(instance)
            relation.save(update_fields=[self.name])

    def pre_save(self, model_instance, add):
        field = getattr(model_instance, self._relation)
        value = field.count()
        setattr(model_instance, self.name, value)
        return value
