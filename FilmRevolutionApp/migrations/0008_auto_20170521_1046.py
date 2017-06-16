# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('FilmRevolutionApp', '0007_auto_20170521_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'M', b'Male'),
                                                          (b'F', b'Female')]),
        ),
        migrations.AlterField(
            model_name='director',
            name='deathday',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'M', b'Male'),
                                                          (b'F', b'Female')]),
        ),
    ]
