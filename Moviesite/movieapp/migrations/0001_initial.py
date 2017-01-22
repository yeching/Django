# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('origin', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('directors', models.CharField(max_length=200)),
                ('casts', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('genres', models.CharField(max_length=200)),
                ('countries', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
