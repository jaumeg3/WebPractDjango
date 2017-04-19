# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmRevolutionApp', '0002_seriereview'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ForeignKey(related_name='ActorM', to='FilmRevolutionApp.Movie', null=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='serie',
            field=models.ForeignKey(related_name='ActorS', to='FilmRevolutionApp.Serie', null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='movie',
            field=models.ForeignKey(related_name='DirectorM', to='FilmRevolutionApp.Movie', null=True),
        ),
        migrations.AddField(
            model_name='director',
            name='serie',
            field=models.ForeignKey(related_name='DirectorS', to='FilmRevolutionApp.Serie', null=True),
        ),
        migrations.AddField(
            model_name='platform',
            name='serie',
            field=models.ForeignKey(to='FilmRevolutionApp.Serie', null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='movie',
            field=models.ForeignKey(to='FilmRevolutionApp.Movie', null=True),
        ),
    ]
