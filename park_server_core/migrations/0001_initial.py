# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Parcheggio',
                'verbose_name_plural': 'Parcheggi',
            },
        ),
        migrations.CreateModel(
            name='ParkData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('capacity', models.IntegerField(default=0)),
                ('full', models.IntegerField(default=0)),
                ('free', models.IntegerField(default=0)),
                ('park', models.ForeignKey(related_name='data', to='park_server_core.Park')),
            ],
            options={
                'ordering': ['park', 'stamp'],
                'verbose_name': 'Dati parcheggio',
                'verbose_name_plural': 'Dati parcheggio',
            },
        ),
        migrations.CreateModel(
            name='ParkStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stamp', models.DateTimeField(auto_now_add=True)),
                ('capacity', models.IntegerField(default=0)),
                ('full', models.IntegerField(default=0)),
                ('free', models.IntegerField(default=0)),
                ('park', models.OneToOneField(related_name='status', to='park_server_core.Park')),
            ],
            options={
                'ordering': ['park', 'stamp'],
                'verbose_name': 'Stato parcheggio',
                'verbose_name_plural': 'Stati parcheggio',
            },
        ),
    ]
