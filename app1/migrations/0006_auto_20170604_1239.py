# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-04 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_samochod_rok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samochod',
            name='nadwozie',
            field=models.CharField(choices=[(b'Kombi', b'Kombi'), (b'Sedan', b'Sedan'), (b'Hatchback', b'Hatchback'), (b'Kabriolet', b'Kabriolet'), (b'SUV', b'SUV'), (b'Coupe', b'Coupe')], max_length=20),
        ),
        migrations.AlterField(
            model_name='samochod',
            name='paliwo',
            field=models.CharField(choices=[(b'Benzyna', b'Benzyna'), (b'Diesel', b'Diesel'), (b'LPG', b'LPG')], max_length=20),
        ),
    ]
