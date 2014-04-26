from django.test import TestCase
from flexmock import flexmock
from should_dsl import should

from tests.models import MultiFieldSlug
from tests.models import CachedCounterModel


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
    def test_should_read_from_getter_function(self):
        model = CachedCounterModel()
        model.fakerelation = relationship_mock = flexmock()

        (
            relationship_mock.should_receive('count')
            .with_args()
            .and_return(10)
            .once()
        )

        model.save()
        model.counter | should | equal_to(10)

    def test_should_update_on_every_save(self):
        model = CachedCounterModel()
        model.fakerelation = relationship_mock = flexmock()

        (
            relationship_mock.should_receive('count')
            .with_args()
            .and_return(10)
            .and_return(20)
            .twice()
        )

        model.save()
        model.counter | should | equal_to(10)

        model.save()
        model.counter | should | equal_to(20)
