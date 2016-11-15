# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_auto_20161115_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='status',
            field=models.CharField(default=b'0', max_length=3, db_index=True, choices=[(b'0', b'Open Alert'), (b'1', b'Send Alert'), (b'2', b'Expired Alert')]),
        ),
    ]
