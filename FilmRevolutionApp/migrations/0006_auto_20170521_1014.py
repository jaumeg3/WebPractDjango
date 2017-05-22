# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmRevolutionApp', '0005_auto_20170521_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='serie',
        ),
        migrations.RemoveField(
            model_name='production',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='productor',
            field=models.ForeignKey(to='FilmRevolutionApp.Production', null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='platform',
            field=models.ForeignKey(to='FilmRevolutionApp.Platform', null=True),
        ),
    ]
