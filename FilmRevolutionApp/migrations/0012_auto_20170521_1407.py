# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('FilmRevolutionApp', '0011_auto_20170521_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(max_length=6, choices=[(b'Male', b'Male'), (
            b'Female', b'Female')]),
        ),
        migrations.AlterField(
            model_name='director',
            name='gender',
            field=models.CharField(max_length=6, choices=[(b'Male', b'Male'), (
            b'Female', b'Female')]),
        ),
    ]
