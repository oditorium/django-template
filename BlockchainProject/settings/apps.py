"""
settings package: Django apps related settings
"""
from .settings import environ as _environ


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',
]

if _environ('SSLSERVER'):
    # to launch the sslserver use the following command:
    #    export SSLSERVER=1
    #    export CERTS=/path/to/my/cert
    #    python3 manage.py runsslserver 0.0.0.0:443 --certificate $CERTS.crt --key $CERTS.key
    INSTALLED_APPS += ['sslserver']
