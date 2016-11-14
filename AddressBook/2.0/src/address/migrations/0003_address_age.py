# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20161103_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='age',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
