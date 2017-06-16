# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('birthday', models.TextField()),
                ('deathday', models.TextField()),
                ('gender', models.TextField()),
                ('place', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('birthday', models.TextField()),
                ('deathday', models.TextField()),
                ('gender', models.TextField()),
                ('place', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('budget', models.TextField()),
                ('genere', models.TextField()),
                ('url', models.URLField()),
                ('popularity', models.IntegerField()),
                ('country', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=3,
                                                            verbose_name=b'Rating (stars)',
                                                            choices=[
                                                                (1, b'one'),
                                                                (2, b'two'),
                                                                (3, b'three'),
                                                                (4, b'four'), (
                                                                5, b'five')])),
                ('comment', models.TextField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('movie', models.ForeignKey(to='FilmRevolutionApp.Movie')),
                ('user',
                 models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('genere', models.TextField()),
                ('url', models.URLField()),
                ('popularity', models.IntegerField()),
                ('numberSeasons', models.IntegerField()),
                ('numberChapters', models.IntegerField()),
            ],
        ),
    ]
