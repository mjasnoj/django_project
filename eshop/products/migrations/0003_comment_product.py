# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170112_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
    ]
