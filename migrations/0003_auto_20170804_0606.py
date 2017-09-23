# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_auto_20170610_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBVersion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('develop_version', models.IntegerField()),
                ('major_version', models.IntegerField()),
                ('minor_version', models.IntegerField()),
            ],
            options={
                'db_table': 'dbversion',
            },
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
