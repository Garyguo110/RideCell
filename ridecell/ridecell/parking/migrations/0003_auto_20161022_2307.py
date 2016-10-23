# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20161022_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkinglocation',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(help_text=b'Longitude, Latitude coordinate system', srid=4326),
        ),
    ]
