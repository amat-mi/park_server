# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('park_server_core', '0002_auto_20150901_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkdata',
            name='nowstamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='parkdata',
            name='webstamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='parkstatus',
            name='nowstamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='parkstatus',
            name='webstamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
