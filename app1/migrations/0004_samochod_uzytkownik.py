# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 19:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_uzytkownik'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochod',
            name='uzytkownik',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app1.Uzytkownik'),
        ),
    ]
