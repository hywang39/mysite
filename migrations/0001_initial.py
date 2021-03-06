# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_id', models.IntegerField()),
                ('restaurant_name', models.CharField(max_length=50)),
                ('restaurant_open_hour', models.BigIntegerField()),
                ('restaurant_close_hour', models.BigIntegerField()),
                ('restaurant_address', models.CharField(max_length=50)),
                ('restaurant_phone', models.CharField(max_length=20)),
                ('restaurant_email', models.CharField(max_length=50)),
                ('restaurant_category_id', models.CharField(max_length=20)),
                ('restaurant_description', models.CharField(max_length=200)),
                ('restaurant_score', models.FloatField()),
                ('restaurant_area', models.CharField(max_length=20)),
                ('restaurant_revenue', models.FloatField()),
                ('restaurant_num_recommendation', models.IntegerField()),
                ('restaurant_picture', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Restaurant',
            },
        ),
    ]
