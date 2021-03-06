# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-03 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('test_res', models.CharField(blank=True, default='', max_length=100)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
