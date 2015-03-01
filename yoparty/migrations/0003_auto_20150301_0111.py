# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yoparty', '0002_yomember_show_help'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yomember',
            name='lat',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='yomember',
            name='lng',
            field=models.FloatField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
