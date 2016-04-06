import os
try:
    import json
except:
    import simplejson as json
from random import randint

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.exceptions import EasyThumbnailsError
from easy_thumbnails.files import get_thumbnailer

from filer.settings import FILER_STATICMEDIA_PREFIX as static_prefix
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from cmsplugin_filer_image import models
from cmsplugin_filer_image.models import ThumbnailOption


class FilerImagePluginForm(forms.ModelForm):
    class Meta:
        model = models.FilerImage
        exclude = ()

    def __init__(self, *args, **kwargs):
        # hide related buttons for page link
        page_link_widget = self.base_fields['page_link'].widget
        page_link_widget.can_add_related = \
            page_link_widget.can_change_related = \
            page_link_widget.can_delete_related = False
        super(FilerImagePluginForm, self).__init__(*args, **kwargs)

        link_options_field = self.fields.get('link_options', None)
        # the values are css classes of the formsets that are shown/hidden
        # when link_options is changed
        formset_divs_cls = {
            models.FilerImage.OPT_NO_LINK: 'None',
            models.FilerImage.OPT_ADD_LINK: '.form-row.field-free_link.field-target_blank',
            models.FilerImage.OPT_PAGE_LINK: '.form-row.field-page_link',
            models.FilerImage.OPT_FILE_LINK: '.form-row.field-file_link',
        }
        if link_options_field:
            # this attr will be used in link_options.js
            link_options_field.widget.attrs = {
                'data': json.dumps(formset_divs_cls)
            }

        qs = ThumbnailOption.objects.get_default_options(
            self.instance.has_attached_image())
        self.fields['thumbnail_option'].widget.choices.queryset = qs

        caption_credit_img = ('%sadmin/img/image-caption-credit.jpg'
                              % (settings.STATIC_URL))

        popup_html = _("<span class='help-button' data-rel='popover' "
                       "data-trigger='hover' data-placement='right' "
                       "data-content='<img src=%s/>' "
                       "data-original-title='' title=''>?</span>"
                       % (caption_credit_img))
        self.fields['image'].widget.attrs.update({'helper_popup': popup_html})
        self.fields['alt_text'].widget.attrs.update(
            {'data-message_when_empty': _("Strongly recommended")})

    def clean_free_link(self):
        link_options = self.cleaned_data['link_options']
        if (link_options == self.instance.OPT_ADD_LINK and
            not self.cleaned_data.get('free_link', '')):
            raise ValidationError('Link filed is required!')
        return self.cleaned_data['free_link']

    def clean_page_link(self):
        link_options = self.cleaned_data['link_options']
        if (link_options == self.instance.OPT_PAGE_LINK and
            not self.cleaned_data.get('page_link', None)):
            raise ValidationError('Page link is required!')
        return self.cleaned_data['page_link']

    def clean_file_link(self):
        link_options = self.cleaned_data['link_options']
        if (link_options == self.instance.OPT_FILE_LINK and
            not self.cleaned_data.get('file_link', None)):
            raise ValidationError('File link is required!')
        return self.cleaned_data['file_link']

    def clean_event_category(self):
        enable_event_tracking = self.cleaned_data['enable_event_tracking']
        link_options = self.cleaned_data['link_options']
        if (enable_event_tracking and
            link_options != self.instance.OPT_NO_LINK and
            not self.cleaned_data.get('event_category', None)):
            raise ValidationError('Event category is required!')
        return self.cleaned_data['event_category']

    def clean_event_action(self):
        enable_event_tracking = self.cleaned_data['enable_event_tracking']
        link_options = self.cleaned_data['link_options']
        if (enable_event_tracking and
            link_options != self.instance.OPT_NO_LINK and
            not self.cleaned_data.get('event_action', None)):
            raise ValidationError('Event action is required!')
        return self.cleaned_data['event_action']

    def save(self, commit=True):
        self._make_thumbnail_if_necessary()
        return super(FilerImagePluginForm, self).save(commit=commit)

    def _make_thumbnail_if_necessary(self):
        """
        Explicitly make a thumbnail for the plugin if this is required.
        The thumbnail is actually created in django-cms edit_plugin view by
        accident because the view gets the image of the cms_plugin. This will
        only make one extra DB select in that case.
        """
        plugin = self.instance
        actual_image = plugin.image
        if not actual_image or not plugin.width and not plugin.height:
            return
        if plugin.width == actual_image.width and plugin.height == actual_image.height:
            return
        options = get_thumbnail_options({}, self.instance)
        self.instance.image.image.file.get_thumbnail(options)


class FilerImagePlugin(CMSPluginBase):
    form = FilerImagePluginForm
    module = 'Filer'
    model = models.FilerImage
    name = _("Image")
    render_template = "cmsplugin_filer_image/image.html"
    text_enabled = True
    raw_id_fields = ('image', 'file_link')
    admin_preview = False
    fieldsets = (
        (None, {
            'fields': (('alt_text',),
                       ('caption_text', 'show_caption'),
                       ('credit_text', 'show_credit'),
                       ('image', ), )
        }),
        (_('Image options'), {
            'fields': ('thumbnail_option',
                       'alignment',
                       'link_options',
                       ('free_link', 'target_blank',),
                       'page_link',
                       'file_link',)
        }),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': (
                ('width', 'height', 'crop', 'maintain_aspect_ratio'),
                ('top_space', 'right_space', 'bottom_space', 'left_space'),
                'border',
                'enable_event_tracking',
                'event_category',
                'event_action',
                'event_label',
            )
        }),
    )

    class Media:
        js = ("admin/js/popup_handling_override.js",
              "admin/js/link_options.js",
              "admin/js/advanced_panel_text_additions.js",
              "admin/js/caption_formatting.js",
              "admin/js/popup_helper_image.js",
              "admin/js/event_tracking.js",)
        css = {
            'all': ("admin/css/filer_image_form.css",)
        }

    def get_thumbnail(self, context, instance):
        if instance.has_attached_image():
            filer_file_field = instance.image.image.file
            thumbnail_options = get_thumbnail_options(context, instance)
            return filer_file_field.get_thumbnail(thumbnail_options)

    def render(self, context, instance, placeholder):
        """
        Render the context needed by the plugin template.
        Preffer to evaluate all attributes here so hidden/lazy operations can be profiled.
        """
        if not instance.image:
            return {}
        options = get_thumbnail_options(context, instance)
        img_size = options["size"]

        if instance.image.width == img_size[0] and instance.image.height == img_size[1]:
            image = instance.image
        else:
            image = get_thumbnailer(instance.image).get_thumbnail(options)

        container_classes = ""
        container_attributes = ""
        if instance.has_valid_caption() and image.width > 200:
            container_classes += " has-caption"
        if instance.has_valid_credit():
            container_classes += " has-credit"
        if instance.overlay_link:
            container_classes += " zoom-in"
        context.update({
            'image_url': image.url,
            'image_width': image.width,
            'image_height': image.height,
            'img_alt': instance.alt,
            'link': instance.link,
            'link_target': '_blank' if instance.target_blank else '_self',
            'overlay_link': instance.overlay_link,
            'caption': instance.caption or '',
            'credit': instance.credit or '',
            'container_style': self.make_container_style(instance, context, image),
            'container_classes': container_classes,
            'container_attributes': container_attributes,
            'details_style': 'width:{}px;'.format(image.width),
            'rnd': 'imagePlugin_{}'.format(randint(10^6, 10**7)),
        })
        if instance.has_valid_event_tracking():
            context['event_tracking'] = {
                'category': instance.event_category,
                'action': instance.event_action,
                'label': instance.event_label or '',
            }
        return context

    def make_container_style(self, plugin, context, image):
        # Styles for images can be set from 2 places:
        #         1. filer image popup
        #         2. right click on the img from text plg and select Alignment option
        # The style set at point 1. can be accessed with instance.style
        # The style set at point 2. can be accessed with context["inherited_from_parent"]["style"]
        # As you can see below, the style set at point 1. have priority
        # The style set at point 2. is taken into account to keep the consistence
        # with all other plugins.
        style = context.get("inherited_from_parent", {}).get("style", "")
        if plugin.alignment == plugin.CENTER:
            style += 'margin: auto; display: block;'
        else:
            style += "float: %s;" % plugin.alignment if plugin.alignment else ""

        if isinstance(plugin.top_space, (int, long)):
            style += "margin-top: {}px;".format(plugin.top_space)

        if isinstance(plugin.bottom_space, (int, long)):
            style += "margin-bottom: {}px;".format(plugin.bottom_space)

        if isinstance(plugin.left_space, (int, long)):
            style += "margin-left: {}px;".format(plugin.left_space)

        if isinstance(plugin.right_space, (int, long)):
            style += "margin-right: {}px;".format(plugin.right_space)

        if plugin.border:
            style += "border: %spx solid black;" % plugin.border

        style += "width:{}px;".format(image.width)
        return style


    def icon_src(self, instance):
        missingfile_icon = os.path.normpath(
            u"%s/icons/missingfile_%sx%s.png" % (static_prefix, 32, 32,))
        if instance.has_attached_image():
            if getattr(settings, 'FILER_IMAGE_USE_ICON', False):
                return instance.image.icons.get('32', missingfile_icon)
            elif instance.image.width and instance.image.height:
                # Fake the context with a reasonable width value because it is not
                # available at this stage
                try:
                    thumbnail = self.get_thumbnail({'width':200}, instance)
                except EasyThumbnailsError:
                    thumbnail = None
                return thumbnail.url if thumbnail else missingfile_icon
        return missingfile_icon


plugin_pool.register_plugin(FilerImagePlugin)


def get_thumbnail_options(context, instance):
    """
    Return the options of the thumbnail that should be displayed for a plugin.
    :param context: dictionary with width or height parameters for the thumbnail
    """
    width, height = None, None
    crop, upscale = False, False
    subject_location = False
    placeholder_width = context.get('width', None)
    placeholder_height = context.get('height', None)

    if instance.width or instance.height:
        # width and height options override everything else
        if instance.width:
            width = instance.width
        if instance.height:
            height = instance.height
        crop = instance.crop
        upscale = instance.upscale
    elif instance.thumbnail_option:
        if instance.thumbnail_option.width:
            width = instance.thumbnail_option.width
        if instance.thumbnail_option.height:
            height = instance.thumbnail_option.height
        crop = instance.thumbnail_option.crop
        upscale = instance.thumbnail_option.upscale
    else:
        if placeholder_width:
            # use the placeholder width as a hint for sizing
            width = int(placeholder_width)
        if placeholder_height:
            height = int(placeholder_height)

    if instance.has_attached_image():
        if instance.image.subject_location:
            subject_location = instance.image.subject_location
        if not height and width:
            # height was not externally defined: use ratio to scale it by the width
            height = int(float(width)*float(instance.image.height)/float(instance.image.width))
        if not width and height:
            # width was not externally defined: use ratio to scale it by the height
            width = int(float(height)*float(instance.image.width)/float(instance.image.height))
        if not width:
            # width is still not defined. fallback the actual image width
            width = instance.image.width
        if not height:
            # height is still not defined. fallback the actual image height
            height = instance.image.height
    return {'size': (width, height),
            'crop': crop,
            'upscale': upscale,
            'subject_location': subject_location}
