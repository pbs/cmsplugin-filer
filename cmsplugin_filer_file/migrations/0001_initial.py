# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerFile',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('target_blank', models.BooleanField(default=False, verbose_name='Open link in new window')),
                ('file', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.SET_NULL, default=None, verbose_name='file', to='filer.File', null=True)),
            ],
            options={
                'db_table': 'cmsplugin_filerfile',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
