# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0006_auto_20150211_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='comments',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
