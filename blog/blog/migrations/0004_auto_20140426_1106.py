# encoding: utf8
from django.db import models, migrations
import blog.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20140424_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.ForeignKey(to='blog.Article', to_field=u'id')),
                ('session_id', models.CharField(max_length=255)),
            ],
            options={
                u'unique_together': set([('article', 'session_id')]),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='like_count',
            field=blog.models.fields.Counter(default=0, editable=False),
            preserve_default=True,
        ),
    ]
