# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import yoparty.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('api_token', models.SlugField(max_length=36)),
                ('passcode', models.SlugField(default=yoparty.models.random_string, max_length=36)),
                ('cb_code', models.SlugField(default=yoparty.models.random_string, max_length=36)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YoMember',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=55)),
                ('lat', models.IntegerField(blank=True, null=True)),
                ('lng', models.IntegerField(blank=True, null=True)),
                ('location_time', models.DateTimeField(blank=True, null=True)),
                ('group', models.ForeignKey(related_name='members', to='yoparty.YoGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
