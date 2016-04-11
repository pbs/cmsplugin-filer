import os

from django.test import TestCase
from django.core.files import File as DjangoFile

from filer.models.imagemodels import Image
from filer.models.filemodels import File
from filer.tests.helpers import create_superuser, create_image

from cmsplugin_filer_image.models import ThumbnailOption, FilerImage
from cmsplugin_filer_image.cms_plugins import FilerImagePlugin


class ThumbnailOptionsTest(TestCase):

    def setUp(self):
        self.superuser = create_superuser()
        self.img = create_image()
        self.filename = os.path.join(os.path.dirname(__file__),
                                 'test.jpg')
        self.img.save(self.filename, 'JPEG')

        self.image = self.create_filer_image()
        self.image.save()

    def tearDown(self):
        try:
            os.remove(self.filename)
        except OSError:
            pass
        for f in File.objects.all():
            f.delete()

    def create_filer_image(self):
        file_obj = DjangoFile(open(self.filename), name='test.jpg')
        image = Image.objects.create(owner=self.superuser,
                                     original_filename='test.jpg',
                                     file=file_obj)
        return image

    def test_20x20_image(self):
        self.image._width = 20
        self.image._height = 20

        qs = ThumbnailOption.objects.get_default_options(self.image)
        self.assertQuerysetEqual(qs,
                                 ['Original -- 20 x 20'],
                                 lambda o: str(o))

    def test_500x500_image(self):
        self.image._width = 500
        self.image._height = 500

        qs = ThumbnailOption.objects.get_default_options(self.image)
        self.assertQuerysetEqual(qs,
                                 ['Original -- 500 x 500',
                                  'Medium -- 320 x XXX',
                                  'Small -- 180 x XXX'],
                                 lambda o: str(o))

    def test_720x405_image(self):
        self.image._width = 720
        self.image._height = 405

        qs = ThumbnailOption.objects.get_default_options(self.image)
        self.assertQuerysetEqual(qs,
                                 ['Original -- 720 x 405', 'Large -- 616 x XXX',
                                  'Medium -- 320 x XXX', 'Small -- 180 x XXX'],
                                 lambda o: str(o))

    def test_1920x1080_image(self):
        self.image._width = 1920
        self.image._height = 1080

        qs = ThumbnailOption.objects.get_default_options(self.image)
        self.assertQuerysetEqual(qs,
                                 ['Original -- 1024 x 576', 'Large -- 616 x XXX',
                                  'Medium -- 320 x XXX', 'Small -- 180 x XXX'],
                                 lambda o: str(o))


class RenderingTest(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.superuser = create_superuser()
        self.img = create_image()
        self.filename = os.path.join(os.path.dirname(__file__), 'test.jpg')
        self.img.save(self.filename, 'JPEG')
        self.image = self.create_filer_image()
        self.image.save()
        self.filer_image = FilerImage.objects.create(image=self.image)

    def create_filer_image(self):
        file_obj = DjangoFile(open(self.filename), name='test.jpg')
        image = Image.objects.create(owner=self.superuser,
                                     original_filename='test.jpg',
                                     file=file_obj)
        return image

    def test_create_context(self):
        plugin = FilerImagePlugin()
        actual_context = plugin.render({}, self.filer_image, None)
        expected_context = {
            'caption': '',
            'container_classes': '',
            'container_style': 'width:800px;',
            'credit': '',
            'details_style': 'width:800px;',
            'image_height': 600,
            'image_url': self.image.url,
            'image_width': 800,
            'img_alt': 'test.jpg',
            'link': '',
            'link_target': '_self',
            'overlay_link': ''
        }
        self.assertEqual(expected_context, actual_context)

    def test_create_context_all_options(self):
        self.filer_image.alt_text = "alt value"
        self.filer_image.caption_text = "caption value"
        self.filer_image.credit_text = "credit value"
        self.filer_image.show_caption = True
        self.filer_image.show_credit = True
        self.filer_image.link_options = 2
        self.filer_image.free_link = "link address"
        self.filer_image.target_blank = True
        self.filer_image.width = 201
        self.filer_image.height = 300
        self.filer_image.maintain_aspect_ratio = True
        self.filer_image.left_pace = 1
        self.filer_image.right_pace = 2
        self.filer_image.top_pace = 3
        self.filer_image.bottom_pace = 4
        self.filer_image.border = 5
        self.filer_image.enable_event_tracking = True
        self.filer_image.event_category = "event category"
        self.filer_image.event_action = "event action"
        self.filer_image.event_label = "event label"

        plugin = FilerImagePlugin()
        actual_context = plugin.render({}, self.filer_image, None)
        image_url = actual_context.pop('image_url')
        self.assertTrue("201x300" in image_url, "Image is not resized!")
        expected_context = {
            'caption': 'caption value',
            'container_classes': 'has-caption has-credit',
            'container_style': 'border: 5px solid black;width:201px;',
            'credit': 'credit value',
            'details_style': 'width:201px;',
            'event_tracking': {
                'action': 'event action',
                'category': 'event category',
                'label': 'event label',
            },
            'image_height': 151,
            'image_width': 201,
            'img_alt': 'alt value',
            'link': 'link address',
            'link_target': '_blank',
            'overlay_link': ''}
        self.assertEqual(expected_context, actual_context)
