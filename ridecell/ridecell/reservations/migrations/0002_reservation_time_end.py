# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 15, 0, 18, 44, 669623)),
        ),
    ]
