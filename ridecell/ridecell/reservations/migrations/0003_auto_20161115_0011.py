# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ridecell.reservations.models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_reservation_time_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time_end',
            field=models.DateTimeField(default=ridecell.reservations.models.time_end_offset),
        ),
    ]
