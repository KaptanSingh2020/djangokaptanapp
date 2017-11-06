# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tense_check', '0006_auto_20171105_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='tense_choice',
            field=models.CharField(choices=[('past simple positive', 'past simple positive'), ('past simple negative', 'past simple negative'), ('past simple yes-no question', 'past simple yes-no question')], default='past simple positive', max_length=50, null=True),
        ),
    ]