# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0002_delete_duplicate_thumbnailoptions'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='thumbnailoption',
            unique_together=set([('name', 'width', 'height', 'crop', 'upscale')]),
        ),
    ]
