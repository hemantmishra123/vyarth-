# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-04 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bvpapp', '0002_auto_20181004_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='generator',
            name='favorite_fruit',
            field=models.CharField(choices=[('orange', 'Oranges'), ('cantaloupe', 'Cantaloupes'), ('mango', 'Mangoes'), ('honeydew', 'Honeydews')], default='orange', max_length=6),
        ),
    ]
