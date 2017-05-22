# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('FilmRevolutionApp', '0008_auto_20170521_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(120), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='actor',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='actor',
            name='deathday',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='director',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(120), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='director',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='director',
            name='deathday',
            field=models.DateField(null=True, blank=True),
        ),
    ]
