# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0002_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='date',
            field=models.DateField(default=datetime.date(2015, 2, 10)),
            preserve_default=False,
        ),
    ]
