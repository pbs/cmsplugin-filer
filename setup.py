import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "cmsplugin-filer",
    version = "0.9.4pbs25",
    url = 'http://github.com/stefanfoulis/cmsplugin-filer',
    license = 'BSD',
    description = "django-cms plugins for django-filer",
    long_description = read('README.rst'),
    author = 'Stefan Foulis',
    author_email = 'stefan.foulis@gmail.com',
    packages = find_packages(),
    #package_dir = {'':'src'},
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'django-filer >= 0.9pbs, <0.9pbs1000',
        'django-cms>=2.3.5pbs,<2.3.5pbs.1000',
    ],
    include_package_data=True,
    zip_safe = False,
)
