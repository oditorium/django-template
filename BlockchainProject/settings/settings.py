"""
settings package: main settings
"""

#https://docs.djangoproject.com/en/1.9/topics/settings/
#https://docs.djangoproject.com/en/1.9/ref/settings/


import os
import dj_database_url as dburl



from . import environ, BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ndxaqj$gf^#k%)3_^#f8$zjl@0cf2f1q^861+0$hhr$oke&m)n'
    # DO NOT FORGET TO CHANGE THE SECRET KEY!

# SECURITY WARNING: don't run with debug turned on in production!
if environ('DJANGO_DEBUG'):
    DEBUG = True

ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'BlockchainProject.urls'
WSGI_APPLICATION = 'BlockchainProject.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/staticfiles'


if environ('HEROKU'):

    # this assumes the on Heroku an environment called 'HEROKU' is set and true'ish
    # the below code adusts the settings accordingly
    #
    # to create an app on Heroku and set the environment set
    #   heroku create
    #   git push heroku +master
    #   heroku config:set HEROKU=1
    #   heroku run python manage.py migrate
    DEBUG = False
    if environ ('HEROKU_DEBUG'):
        print("***** ATTENTION: Debug mode is one (DEBUG is true'ish) *****")
        DEBUG = True
    DATABASES['default'] =  dburl.config()
    DATABASES['default']['CONN_MAX_AGE'] = 500
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
    WSGI_APPLICATION = 'BlockchainProject.wsgi-whitenoise.application'
