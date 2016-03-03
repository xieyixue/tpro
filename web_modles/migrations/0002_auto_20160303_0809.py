# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_modles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='source_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='url',
            name='source_ip',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
