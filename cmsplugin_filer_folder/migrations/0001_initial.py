# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.folder
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerFolder',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('view_option', models.CharField(default=b'list', max_length=10, verbose_name='view option', choices=[(b'list', 'List'), (b'slideshow', 'Slideshow')])),
                ('folder', filer.fields.folder.FilerFolderField(on_delete=django.db.models.deletion.SET_NULL, default=None, to='filer.Folder', null=True)),
            ],
            options={
                'db_table': 'cmsplugin_filerfolder',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
