CHANGELOG
=========

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
