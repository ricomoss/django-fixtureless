from distutils.core import setup

version = ''

LONG_DESCRIPTION = """
=====================================
django-fixtureless
=====================================

django-fixtureless provides an easy way to create model objects within
your Django project for testing purposes.  This is done through
inspection of your database relationships.  All required fields are
randomly filled.  All foreign key relationships will create respective
objects in the same fashion.

.. note:: django-fixtureless only supports Django 2.1 higher and  Python 3.3+.

.. _Django: http://djangoproject.com
"""

setup(
    name='django-fixtureless',
    version=version,
    author='Rico Cordova',
    author_email='rico.cordova@rocksolidbox.com',
    packages=['fixtureless'],
    url='https://github.com/ricomoss/django_fixtureless',
    license='LICENSE.txt',
    description='Test utility to create fixtureless objects in Django.',
    long_description=LONG_DESCRIPTION,
    keywords=['unittest', 'django', 'Python 3'],
)
