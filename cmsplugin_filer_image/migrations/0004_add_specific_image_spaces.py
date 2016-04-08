# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0003_auto_20150812_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerimage',
            name='bottom_space',
            field=models.PositiveIntegerField(help_text='Add space calculated in pixels bellow the image. Default is 15 pixels.', null=True, verbose_name='bottom space', blank=True),
        ),
        migrations.AddField(
            model_name='filerimage',
            name='left_space',
            field=models.PositiveIntegerField(help_text='Add space calculated in pixels on the left of the image. Default is 15 pixels.', null=True, verbose_name='left space', blank=True),
        ),
        migrations.AddField(
            model_name='filerimage',
            name='right_space',
            field=models.PositiveIntegerField(help_text='Add space calculated in pixels on the left of the image. Default is 15 pixels.', null=True, verbose_name='right space', blank=True),
        ),
        migrations.AddField(
            model_name='filerimage',
            name='top_space',
            field=models.PositiveIntegerField(help_text='Add space calculated in pixels on top of the image. Default is 15 pixels.', null=True, verbose_name='top space', blank=True),
        ),
        migrations.AlterField(
            model_name='filerimage',
            name='alt_text',
            field=models.CharField(help_text='Strongly recommended. Describes the essence of the image for users who have images turned off in their browser, or are visually impaired and using a screen reader; and it is useful to identify images to search engines', max_length=255, null=True, verbose_name='alt text', blank=True),
        ),
    ]
