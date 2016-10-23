# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=15, blank=True)),
                ('stripe_customer_id', models.CharField(unique=True, max_length=255, blank=True)),
                ('last4', models.CharField(default=None, max_length=4, blank=True)),
                ('brand', models.CharField(default=None, max_length=99, blank=True)),
                ('expiration_date', models.DateField(default=None, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
