# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('park_server_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='title',
            field=models.CharField(unique=True, max_length=80),
        ),
    ]
