from django.conf.urls import *

urlpatterns = patterns('cmsplugin_filer_image.views',
    (r'^cmsplugin_filer_image/fetch_image_metadata$', 'fetch_image_metadata'),
)
