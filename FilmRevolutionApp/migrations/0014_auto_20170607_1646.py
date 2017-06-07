# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmRevolutionApp', '0013_auto_20170525_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='serie',
        ),
        migrations.RemoveField(
            model_name='director',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='director',
            name='serie',
        ),
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ForeignKey(to='FilmRevolutionApp.Actor', null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(to='FilmRevolutionApp.Director', null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='actor',
            field=models.ForeignKey(to='FilmRevolutionApp.Actor', null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='director',
            field=models.ForeignKey(to='FilmRevolutionApp.Director', null=True),
        ),
    ]
