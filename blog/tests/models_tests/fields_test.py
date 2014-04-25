from django.test import TestCase
from should_dsl import should

from tests.models import MultiFieldSlug


class AutoSlugFieldComponentTestCase(TestCase):
    def test_should_automatically_create_slug_for_multiple_fields(self):
        instance = MultiFieldSlug(
            field_one='this is field one',
            field_two='and %^# this is field two',
            field_three='and this is three!!!'
        )
        instance.save()

        instance.slug | should | equal_to(
            'this-is-field-one-and-this-is-field-two-and-this-is-three'
        )
