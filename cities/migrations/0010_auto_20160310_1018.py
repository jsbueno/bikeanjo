# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0009_load_countries'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityAlias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.CharField(max_length=63, verbose_name='Alias', db_index=True)),
            ],
            options={
                'verbose_name': 'Alias',
                'verbose_name_plural': 'Aliases',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='coords',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='tz',
            field=models.CharField(max_length=40, verbose_name='Timezone', blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='cities.State', null=True),
        ),
        migrations.AddField(
            model_name='cityalias',
            name='city',
            field=models.ForeignKey(to='cities.City'),
        ),
    ]
