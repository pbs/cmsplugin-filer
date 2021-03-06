SOUTH_TESTS_MIGRATE = False

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'mptt',
    'cms',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
]

FILER_ENABLE_PERMISSIONS = True
FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True
FILER_IS_PUBLIC_DEFAULT = True
SECRET_KEY = 'abscd'
STATIC_ROOT = '/static/'
STATIC_URL = '/static/'
ROOT_URLCONF = 'cmsplugin_filer_image.tests.urls'
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    'django.contrib.messages.context_processors.messages',
    "django.template.context_processors.i18n",
    "django.template.context_processors.debug",
    "django.template.context_processors.request",
    "django.template.context_processors.media",
    'django.template.context_processors.csrf',
    "sekizai.context_processors.sekizai",
    "django.template.context_processors.static",
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : 'test.db', # Or path to database file if using sqlite3.
        'USER' : '', # Not used with sqlite3.
        'PASSWORD' : '', # Not used with sqlite3.
        'HOST' : '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT' : '', # Set to empty string for default. Not used with sqlite3.
    }
}
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    )

FILER_CDN_DOMAIN = 'bento.cdn.pbs.org'
FILER_STORAGES = {
    'public': {
        'main': {
            'ENGINE': 'django.core.files.storage.FileSystemStorage',
            'OPTIONS': {
                'location': 'hostedbento-test',
                },
            'UPLOAD_TO': 'filer.utils.generate_filename.by_date',
            'UPLOAD_TO_PREFIX': 'filer_public',
            },
        'thumbnails': {
            'ENGINE': 'django.core.files.storage.FileSystemStorage',
            'OPTIONS': {
                'location': 'hostedbento-test',
                },
            'THUMBNAIL_OPTIONS': {
                'base_dir': 'filer_public_thumbnails',
                },
            },
        },
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}
