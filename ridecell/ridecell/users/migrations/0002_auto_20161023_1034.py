# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='brand',
            field=models.CharField(max_length=99, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='expiration_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last4',
            field=models.CharField(max_length=4, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='stripe_customer_id',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
