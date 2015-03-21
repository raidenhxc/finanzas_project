# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0005_auto_20150210_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='comments',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='movement',
            name='concept',
            field=models.ForeignKey(to='finanzas.Concept'),
        ),
    ]
