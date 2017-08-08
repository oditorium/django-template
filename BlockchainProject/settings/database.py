"""
settings package: database related settings
"""
from . import environ, BASE_DIR

import os


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
if environ('DJANGO_USE_SQLITE'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': '/etc/apache2/my.cnf', # contains credentials
            },
        'NAME': 'dbname',
        }
    }
