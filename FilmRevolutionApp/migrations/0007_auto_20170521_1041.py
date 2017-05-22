# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('FilmRevolutionApp', '0006_auto_20170521_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='director',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='platform',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='production',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
