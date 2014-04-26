from django.test import TestCase
from flexmock import flexmock
from should_dsl import should

from tests.models import MultiFieldSlug
from tests.models import CachedCounterModel
from tests.models import CachedCounterRelation


class AutoSlugFieldComponentTestCase(TestCase):
    def test_should_automatically_create_slug_for_multiple_fields(self):
        instance = MultiFieldSlug.objects.create(
            field_one='this is field one',
            field_two='and %^# this is field two',
            field_three='and this is three!!!'
        )

        instance.slug | should | equal_to(
            'this-is-field-one-and-this-is-field-two-and-this-is-three'
        )


class CouterFieldComponentTestCase(TestCase):
    def test_should_read_from_relation_count_and_update_on_save(self):
        model = CachedCounterModel.objects.create()
        model.counter | should | equal_to(0)

        for count in xrange(1, 10):
            CachedCounterRelation.objects.create(other=model)
            model.counter | should | equal_to(count)

    def test_should_read_from_relation_count_and_update_on_delete(self):
        model = CachedCounterModel.objects.create()
        model.counter | should | equal_to(0)

        for count in xrange(1, 10):
            CachedCounterRelation.objects.create(other=model)

        for count in xrange(8, -1, -1):
            model.relation.latest('id').delete()
            model.counter | should | equal_to(count)
