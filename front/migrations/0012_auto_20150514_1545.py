# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0011_auto_20150507_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helprequest',
            name='accepted',
        ),
        migrations.AlterField(
            model_name='helprequest',
            name='status',
            field=models.CharField(default=b'new', max_length=16, choices=[(b'new', 'New'), (b'open', 'Open'), (b'attended', 'Attended'), (b'finalized', 'Finalized'), (b'canceled', 'Canceled')]),
        ),
    ]
