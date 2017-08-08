"""
settings package: logging related settings
"""
# https://docs.djangoproject.com/en/1.11/topics/logging/

import logging
import os

from . import BASE_DIR


##########################################################
## LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {},
    'handlers': {},
    'filters': {},
    'formatters': {},
}


##########################################################
## LOGGERS
_L = LOGGING['loggers']
_L['']      = {'handlers': ['consoledbh', 'consoleh'], 'level': 'DEBUG'}
_L['data']  = {'handlers': ['datafh'], 'level': 'DEBUG', 'propagate': False}
_L['datac'] = {'handlers': ['datach'], 'level': 'DEBUG', 'propagate': False}
_L['event'] = {'handlers': ['eventfh', 'consoleh'], 'level': 'INFO', 'propagate': False}


##########################################################
## HANDLERS
_H = LOGGING['handlers']

##########################################
## CONSOLEH (handler)
_H['consoleh'] = {
    'formatter': 'verbose',
    'filters': [],
    'class': 'logging.StreamHandler',
    'level': 'INFO',
}

##########################################
## CONSOLEDBH (handler)
_H['consoledbh'] = LOGGING['handlers']['consoleh'].copy()
_H['consoledbh']['filters'] = ['debugmodef']

##########################################
## EVENTFH (handler)
_H['eventfh'] = {
    'formatter': 'verbose',
    'filename': os.path.join(BASE_DIR, 'event.log'),
    'class': 'logging.FileHandler',
    'level': 'DEBUG',
    'filters': []
}

##########################################
## DATAFH (handler)
_H['datafh'] = {
    'formatter': 'datat',
    'filename': os.path.join(BASE_DIR, 'data.log'),
    'class': 'logging.FileHandler',
    'level': 'DEBUG',
    'filters': []
}

##########################################
## DATACH (handler)
_H['datach'] = {
    'formatter': 'datat',
    'filters': [],
    'class': 'logging.StreamHandler',
    'level': 'DEBUG'
}


##########################################################
## FILTERS
_R = LOGGING['filters']
_R['debugmodef'] = {'()': 'django.utils.log.RequireDebugTrue'}


##########################################################
## FORMATTERS
_F = LOGGING['formatters']

_F['simple']   = {'format': '%(levelname)s %(message)s'}
_F['standard'] = {'format': '%(levelname)s %(asctime)s %(name)s %(message)s'}
_F['verbose']  = {'format': '%(levelname)s [%(pathname)s] at %(created)s (%(asctime)s) >> %(message)s'}

_F['data']     = {'format': '%(message)s'}
_F['datat']    = {'format': '%(created)f, %(message)s'}
