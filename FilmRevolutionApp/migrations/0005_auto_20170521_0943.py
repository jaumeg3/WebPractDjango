# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FilmRevolutionApp', '0004_auto_20170419_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='place',
        ),
        migrations.RemoveField(
            model_name='director',
            name='place',
        ),
        migrations.AddField(
            model_name='actor',
            name='city',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='actor',
            name='country',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='actor',
            name='state',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='director',
            name='city',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='director',
            name='country',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='director',
            name='state',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='deathday',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='movie',
            field=models.ForeignKey(related_name='ActorM', blank=True, to='FilmRevolutionApp.Movie', null=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='serie',
            field=models.ForeignKey(related_name='ActorS', blank=True, to='FilmRevolutionApp.Serie', null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='deathday',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='movie',
            field=models.ForeignKey(related_name='DirectorM', blank=True, to='FilmRevolutionApp.Movie', null=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='serie',
            field=models.ForeignKey(related_name='DirectorS', blank=True, to='FilmRevolutionApp.Serie', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='serie',
            name='numberChapters',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='serie',
            name='numberSeasons',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='serie',
            name='popularity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
