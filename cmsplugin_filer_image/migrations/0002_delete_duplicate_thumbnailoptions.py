from django.db import migrations
from django.db.models import Count, Max


def forward(apps, schema_editor):
    """
    Get all the duplicates for ThumbnailOption.
    Point each FilerImage where the duplicates are used to the correct
    ThumbnailOption.
    Delete remaining ThumbnailOption duplicates.
    """
    ThumbnailOption = apps.get_model("cmsplugin_filer_image", "ThumbnailOption")
    unique_fields = ["name", "width", "height", "crop", "upscale"]
    duplicates = (ThumbnailOption.objects.values(*unique_fields)
                  .order_by()
                  .annotate(max_id=Max('id'), count_id=Count('id'))
                  .filter(count_id__gt=1))

    for duplicate in duplicates:
        for thumbnail_option in ThumbnailOption.objects.filter(
                **{x: duplicate[x] for x in unique_fields}
        ).exclude(id=duplicate['max_id']):
            for filer_image in thumbnail_option.filerimage_set.all():
                filer_image.thumbnail_option_id = duplicate['max_id']
            thumbnail_option.delete()


class Migration(migrations.Migration):
    dependencies = [('cmsplugin_filer_image', '0001_initial'),]
    operations = [migrations.RunPython(forward)]
