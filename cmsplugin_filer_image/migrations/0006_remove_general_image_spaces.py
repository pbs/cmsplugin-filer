# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0005_specialize_image_margins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filerimage',
            name='horizontal_space',
        ),
        migrations.RemoveField(
            model_name='filerimage',
            name='vertical_space',
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='bottom_space',
            field=models.PositiveIntegerField(help_text='Add space calculated in pixels bellow the image. Default is 12 pixels.', null=True, verbose_name='bottom space', blank=True),
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='left_space',
            field=models.PositiveIntegerField(help_text='Add space calculated in pixels on the left of the image.', null=True, verbose_name='left space', blank=True),
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='right_space',
            field=models.PositiveIntegerField(help_text='Add space calculated in pixels on the right of the image.', null=True, verbose_name='right space', blank=True),
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='top_space',
            field=models.PositiveIntegerField(help_text='Add space calculated in pixels on top of the image.', null=True, verbose_name='top space', blank=True),
        ),
    ]
