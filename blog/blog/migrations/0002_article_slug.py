# encoding: utf8
from django.db import models, migrations
import blog.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=blog.models.fields.AutoSlugField(default='nonreversible-migration-default', editable=False),
            preserve_default=False,
        ),
    ]
