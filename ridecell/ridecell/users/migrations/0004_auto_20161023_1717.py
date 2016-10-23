# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161023_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='brand',
            new_name='cc_brand',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='expiration_date',
            new_name='cc_expiration_date',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='last4',
            new_name='cc_last4',
        ),
    ]
