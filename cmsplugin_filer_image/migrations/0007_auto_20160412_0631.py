# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0006_remove_general_image_spaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerimage',
            name='alignment',
            field=models.CharField(choices=[(b'center', 'center'), (b'left', 'left'), (b'right', 'right')], max_length=10, blank=True, help_text='When inside a text component, text will wrap around images with a left or right alignment; text will not wrap around an image with a center alignment.', null=True, verbose_name='image alignment'),
        ),
    ]
