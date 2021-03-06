from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.file import FilerFileField
from cmsplugin_filer_utils import FilerPluginManager
from urlparse import urlparse
import filer


class FilerFile(CMSPlugin):
    """
    Plugin for storing any type of file.

    Default template displays download link with icon (if available) and file size.

    This could be updated to use the mimetypes library to determine the type of file rather than
    storing a separate icon for each different extension.

    The icon search is currently performed within get_icon_url; this is probably a performance concern.
    """
    title = models.CharField(_("title"), max_length=255, null=True, blank=True)
    file = FilerFileField(default=None, null=True, on_delete=models.SET_NULL,
                          verbose_name=_('file'))
    target_blank = models.BooleanField(_('Open link in new window'), default=False)

    objects = FilerPluginManager(select_related=('file',))

    class Meta:
        db_table = 'cmsplugin_filerfile'

    def has_attached_file(self):
        try:
            return self.file
        except filer.models.File.DoesNotExist:
            return None

    def get_icon_url(self):
        return self.file.icons['32'] if self.has_attached_file() else None

    def is_absolute_url(self):
        return bool(urlparse(self.get_icon_url() or '').netloc)

    def file_exists(self):
        if not self.has_attached_file():
            return False
        return self.file.file.storage.exists(self.file.file.name)

    def get_file_name(self):
        if not self.has_attached_file():
            return ''
        if self.file.name in ('', None):
            name = u"%s" % (self.file.original_filename,)
        else:
            name = u"%s" % (self.file.name,)
        return name

    def get_ext(self):
        return self.file.extension

    def __unicode__(self):
        if self.title:
            return self.title
        if self.has_attached_file():
            return self.get_file_name()
        return "<empty>"

    search_fields = ('title',)
