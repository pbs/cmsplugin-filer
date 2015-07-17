# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerImage',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('alt_text', models.CharField(help_text='Describes the essence of the image for users who have images turned off in their browser, or are visually impaired and using a screen reader; and it is useful to identify images to search engines', max_length=255, null=True, verbose_name='alt text', blank=True)),
                ('caption_text', models.CharField(help_text='Caption text is displayed directly below an image to add context; there is a 140-character limit, including spaces; for images fewer than 200 pixels wide, the caption text is only displayed on hover', max_length=140, null=True, verbose_name='caption text', blank=True)),
                ('credit_text', models.CharField(help_text='Credit text gives credit to the owner or licensor of an image; it is displayed below the image,<br>or below the caption text if that option is selected; there is a 30-character limit, including spaces.', max_length=30, null=True, verbose_name='credit text', blank=True)),
                ('show_caption', models.BooleanField(default=False, verbose_name='show caption text')),
                ('show_credit', models.BooleanField(default=False, verbose_name='show credit text')),
                ('alignment', models.CharField(choices=[(b'center', 'center'), (b'left', 'left'), (b'right', 'right')], max_length=10, blank=True, help_text='When inside a text plugin, text will wrap around images with a left or right alignment; text will not wrap around an image with a center alignment.', null=True, verbose_name='image alignment')),
                ('link_options', models.IntegerField(default=1, help_text='This menu provieds options for linking the image to another file, another page, a document, or to open up the image in its original size; making a selection via the dropdown will generate the  required admin fields.', verbose_name='link image options', choices=[(1, b'No link'), (2, b'Add link'), (3, b'Link to page'), (4, b'Link to document/media'), (5, b'Open original image in overlay')])),
                ('free_link', models.CharField(help_text='if present image will be clickable', max_length=255, null=True, verbose_name='link', blank=True)),
                ('target_blank', models.BooleanField(default=False, verbose_name='Open link in new window')),
                ('width', models.PositiveIntegerField(null=True, verbose_name='width', blank=True)),
                ('height', models.PositiveIntegerField(null=True, verbose_name='height', blank=True)),
                ('crop', models.BooleanField(default=False, verbose_name='crop')),
                ('maintain_aspect_ratio', models.BooleanField(default=True, verbose_name='maintain aspect ratio')),
                ('vertical_space', models.PositiveIntegerField(null=True, verbose_name='vertical space', blank=True)),
                ('horizontal_space', models.PositiveIntegerField(help_text='Add spacing or padding around the image; calculated in pixels; if left blank, the vertical spacing will default to 15 pixels.', null=True, verbose_name='horizontal space', blank=True)),
                ('border', models.PositiveIntegerField(help_text='Add a black border around the image; the input is the pixel width of the line; there is no line if left blank.', null=True, verbose_name='border', blank=True)),
                ('enable_event_tracking', models.BooleanField(default=False, verbose_name='Enable event tracking')),
                ('event_category', models.CharField(max_length=30, null=True, verbose_name='Event category', blank=True)),
                ('event_action', models.CharField(max_length=30, null=True, verbose_name='Event action', blank=True)),
                ('event_label', models.CharField(max_length=30, null=True, verbose_name='Event label', blank=True)),
                ('upscale', models.BooleanField(default=True, verbose_name='upscale')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('use_original_image', models.BooleanField(default=False, help_text='do not resize the image. use the original image instead.', verbose_name='use the original image')),
                ('original_link', models.BooleanField(default=False, help_text='if present image will be clickable', verbose_name='link original image')),
                ('use_autoscale', models.BooleanField(default=False, help_text='tries to auto scale the image based on the placeholder context', verbose_name='use automatic scaling')),
                ('file_link', filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, default=None, to='filer.File', blank=True, help_text='if present image will be clickable', null=True, verbose_name='file link')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='filer.Image', null=True, verbose_name='image')),
                ('page_link', models.ForeignKey(blank=True, to='cms.Page', help_text='if present image will be clickable', null=True, verbose_name='page link')),
            ],
            options={
                'db_table': 'cmsplugin_filerimage',
                'verbose_name': 'filer image',
                'verbose_name_plural': 'filer images',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ThumbnailOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('width', models.IntegerField(help_text='width in pixel.', verbose_name='width')),
                ('height', models.IntegerField(help_text='height in pixel.', verbose_name='height')),
                ('crop', models.BooleanField(default=True, verbose_name='crop')),
                ('upscale', models.BooleanField(default=True, verbose_name='upscale')),
            ],
            options={
                'ordering': ('-width',),
                'verbose_name': 'thumbnail option',
                'verbose_name_plural': 'thumbnail options',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='filerimage',
            name='thumbnail_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cmsplugin_filer_image.ThumbnailOption', help_text='The most common image options are available via this drop-down menu; to add a custom size, use the advanced options menu below; any advanced option selection will override the settings in this admin.', null=True, verbose_name='image size'),
            preserve_default=True,
        ),
    ]
