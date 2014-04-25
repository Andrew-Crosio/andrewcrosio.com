from datetime import datetime
from datetime import timedelta

from django.test import TestCase
from should_dsl import should

from tests.models import DatedModel


class CreatedAtAndUpdatedAtModelComponentTestCase(TestCase):
    def test_should_add_field_times_at_creation(self):
        instance = DatedModel()
        instance.save()

        # Make datetimes timezone unaware for comparison
        created_at = instance.created_at.replace(tzinfo=None)
        updated_at = instance.updated_at.replace(tzinfo=None)

        created_at_delta = (datetime.now() - created_at).total_seconds()
        updated_at_delta = (datetime.now() - updated_at).total_seconds()

        created_at_delta | should | be_less_than(5)
        updated_at_delta | should | be_less_than(5)

    def test_should_not_update_creation_field_on_updates(self):
        instance = DatedModel()
        instance.save()

        # Due to the way Django works, need to resave with an offset datetime after creation
        instance.created_at = datetime.now() - timedelta(days=10)
        instance.save()

        # Now we check if it changes
        instance.save()
        delta = (datetime.now() - instance.created_at.replace(tzinfo=None))
        delta.days | should | equal_to(10)

    def test_should_update_updated_field_on_updates(self):
        instance = DatedModel()
        instance.save()

        # Now we reset and force the field pre_save to not be called
        instance.updated_at = datetime.now() - timedelta(days=999)
        instance.save_base(raw=True)
        instance.updated_at.year | should | be_less_than(datetime.now().year)

        instance.save()
        delta = (datetime.now() - instance.updated_at.replace(tzinfo=None)).total_seconds()
        delta | should | be_less_than(10)
