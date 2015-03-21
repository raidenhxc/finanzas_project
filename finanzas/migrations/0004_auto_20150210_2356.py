# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0003_movement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
