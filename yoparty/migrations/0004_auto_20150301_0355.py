# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoparty', '0003_auto_20150301_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='yogroup',
            name='location_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='yogroup',
            name='location_type',
            field=models.SlugField(default='M', max_length=1, choices=[('M', 'Mean'), ('L', 'Location of first user'), ('U', 'User closer to the mean')]),
            preserve_default=True,
        ),
    ]
