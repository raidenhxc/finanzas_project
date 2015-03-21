# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0008_exercise_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='concept',
            field=models.ForeignKey(to='finanzas.Concept', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
