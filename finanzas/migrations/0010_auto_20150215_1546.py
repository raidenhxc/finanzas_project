# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0009_auto_20150215_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='period',
            field=models.ForeignKey(editable=False, to='finanzas.Period', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='period',
            name='exercise',
            field=models.ForeignKey(to='finanzas.Exercise', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
