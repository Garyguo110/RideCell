# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('decription', models.CharField(max_length=255, null=True, blank=True)),
                ('price', models.PositiveIntegerField(default=0, help_text=b'The amount in cents to be charged per hour')),
                ('location', django.contrib.gis.db.models.fields.PointField(help_text=b'Lat Long coordinate system', srid=4326)),
                ('capacity', models.PositiveIntegerField(default=0, help_text=b'The number of available lots')),
                ('reserved', models.PositiveIntegerField(default=0, help_text=b'The number of used lots')),
            ],
        ),
    ]
