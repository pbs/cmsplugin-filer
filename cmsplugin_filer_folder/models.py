from django.utils.translation import ugettext_lazy as _
from django.db import models
from cms.models import CMSPlugin, Page
from django.utils.translation import ugettext_lazy as _
from posixpath import join, basename, splitext, exists
from filer.fields.folder import FilerFolderField
from django.conf import settings
from cmsplugin_filer_utils import FilerPluginManager
import filer

VIEW_OPTIONS = getattr(settings, 'CMSPLUGIN_FILER_FOLDER_VIEW_OPTIONS', (("list", _("List")),("slideshow",_("Slideshow"))))

class FilerFolder(CMSPlugin):
    """
    Plugin for storing any type of Folder.

    Default template displays files store inside this folder.
    """
    title = models.CharField(_("title"), max_length=255, null=True, blank=True)
    view_option = models.CharField(_("view option"),max_length=10,
                            choices=VIEW_OPTIONS, default="list")
    folder = FilerFolderField(default=None, null=True,
                              on_delete=models.SET_NULL)

    objects = FilerPluginManager(select_related=('folder',))

    class Meta:
        db_table = 'cmsplugin_filerfolder'

    def has_attached_folder(self):
        try:
            return self.folder
        except filer.models.Folder.DoesNotExist:
            return None

    def __unicode__(self):
        if self.title:
            return self.title
        if self.has_attached_folder():
            return self.folder.name
        return "<empty>"

    search_fields = ('title',)

