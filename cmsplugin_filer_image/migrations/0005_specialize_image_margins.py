# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import F


def populate_specific_columns_from_old_data(apps, schema_editor):
    """
    Populate specific spacing image fields (top, right, bottom, left) from old general
    spacing image fields (horizontal, vertical).
    """
    FilerImage = apps.get_model("cmsplugin_filer_image", "FilerImage")

    updated_images_cnt = FilerImage.objects.all().update(
        left_space=F('horizontal_space'), right_space=F('horizontal_space'),
        top_space=F('vertical_space'), bottom_space=F('vertical_space'),
    )
    print "Updated new spacing fields for {} images.".format(updated_images_cnt)


def populate_general_columns_from_new_data(apps, schema_editor):
    """
    Populate old general spacing image fields (horizontal, vertical) from new
    specific image fields (top, right, bottom, left).
    """
    FilerImage = apps.get_model("cmsplugin_filer_image", "FilerImage")

    updated_images_cnt = FilerImage.objects.all().update(
        horizontal_space=F('left_space'), vertical_space=F('top_space'),
    )
    print "Updated old spacing fields for {} images.".format(updated_images_cnt)


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_filer_image', '0004_add_specific_image_spaces'),
    ]

    operations = [
        migrations.RunPython(populate_specific_columns_from_old_data,
                             populate_general_columns_from_new_data)
    ]
