CHANGELOG
=========

Revision 395a10e (06.11.2018, 13:19 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Pin pytest 3.4.0 and pytest-django 3.1.2

Revision 44d3f74 (18.10.2016, 11:24 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Fix tests.

Revision 2e3ed05 (15.06.2016, 14:38 UTC)
----------------------------------------

* LUN-2977

  * Handle case when images are deleted in filer and thumbnails cannot be created.

No other commits.

Revision cc620eb (06.05.2016, 15:24 UTC)
----------------------------------------

No new issues.

* Misc commits

  * LUn-2954: Update tooltips.

Revision d1addad (11.04.2016, 08:32 UTC)
----------------------------------------

* LUN-2796

  * Fix tests after refactoring.
  * Review. Removed unneeded code + small refactoring.
  * Ignore test results.
  * Add tests for rendering context rework.
  * Rework image plugin rendering.
  * Specialize image margin options.

No other commits.

Revision e93d6be (20.10.2015, 13:22 UTC)
----------------------------------------

* LUN-2718

  * add specificity to selectors

* LUN-2724

  * fixed credit text on small image

No other commits.

Revision 014acee (13.10.2015, 13:16 UTC)
----------------------------------------

* LUN-2681

  * Image plugin styled to match the style from Photogallery

* Misc commits

  * Remove slicing.
  * Code review improvements:  - drop order_by.  - extract query set in a variable.  - remove max_id.  - call save() for filer_image instance.
  * Fix unexpected multiple ThumbnailOption in filer image plugin.

Revision 904c204 (01.10.2015, 12:24 UTC)
----------------------------------------

* LUN-2677

  * hide related buttons for page link form field

No other commits.

Revision 24ac5d3 (24.09.2015, 11:13 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Django 1.8: removed add/change/delete related buttons from filer widgets
  * Django 1.8: removed add/change/delete related buttons from filer widgets
  * DJango 1.8 upgrade: removed some django1.9 deprecation warnings
  * Django 1.8 upgrade: updated test settings

Revision d78cb65 (12.09.2015, 11:24 UTC)
----------------------------------------

* LUN-2319

  * add spacing to the bottom of image plugin

* LUN-2583

  * Removed preview

No other commits.

Revision 9dd9625 (31.08.2015, 14:26 UTC)
----------------------------------------

* LUN-2287

  * refactor code
  * refactor code + js fix for pop-up helper image
  * refactor code
  * - removed unused css file
  * error messages styled
  * template and css updates according to Ace theme

No other commits.

Revision 34a8446 (30.07.2015, 09:10 UTC)
----------------------------------------

* LUN-2416

  * Fix broken icon.

* Misc commits

  * Improve check of absolute URL. Remove duplicate code.
  * Remove unused import.
  * Improve icon url for proxied sites.

Revision 7b2af0a (17.07.2015, 14:50 UTC)
----------------------------------------

No new issues.

* Misc commits

  * tox: Don't allow django 1.8 prereleases
  * Django 1.7 upgrade: regenerated migrations; fixed deprecation warnings;
  * Django 1.6 upgrade: fixed imports; remove unused imports

Revision f746876 (11.03.2015, 13:58 UTC)
----------------------------------------

No new issues.

* Misc commits

  * move styles from .html to .css
  * z-index as small as possible; minor style change
  * verify that image actually exists
  * overlay on image click works
  * overlay on click almost works

Revision 02b793f (05.11.2014, 09:31 UTC)
----------------------------------------

* LUN-1859

  * _quick Remove template code duplication.
  * _quick Proper formating for templates (use non-wrap mode). Proper closing of <a> tag.
  * _quick Resurect the old logic of having the template serving the original image or the version resized by thumbnailer templatetag.

No other commits.

Revision f76aaf5 (03.07.2014, 07:31 UTC)
----------------------------------------

No new issues.

* Misc commits

  * bumb version as instructed by bamboo
  * refactor by sending context variables
  * Strip caption/credit when checking for content.
  * remove properties and compute everything in template
  * Don't display caption or credit section if empty.

Revision 8e3088d (13.06.2014, 12:16 UTC)
----------------------------------------

* LUN-1206

  * should not generate icon in plugin for images with no with or height.

* LUN-1446

  * add default icon for plugin just in case easy_thumbnails decides to throw InvalidImageFormatError. This is required for the blog migration since we're moving plugins around. Even if the image is not valid plugin data should be migrated.

* Misc commits

  * SHould not throw 500 if filer image was trashed.
  * Provided default image icon for image plugin even if thumbnails cannot get generated.

Revision fc7fef7 (06.05.2014, 15:15 UTC)
----------------------------------------

* LUN-1548

  * : fix image event tracking not saving the first time

* LUN-1549

  * : update GA event tracking help text in admin

No other commits.

Revision 5f69b25 (23.04.2014, 07:15 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Bump version as instructed by bamboo

Revision d1118a8 (17.04.2014, 15:55 UTC)
----------------------------------------

* LUN-1450

  * : Minor comment refactor
  * : Add GA event tracking for clickable images

No other commits.

Revision 5e56340 (17.04.2014, 13:22 UTC)
----------------------------------------

Changelog history starts here.
