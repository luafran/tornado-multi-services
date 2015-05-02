"""
Settings used in unit/component tests environments
"""
import os

ENVIRONMENT_NAME = 'UNIT_TESTS'

AUTO_RELOAD = True

STATS_ENABLED = False
STATS_SERVICE_HOSTNAME = '54.164.227.227'

ENFORCE_POLICIES = False

LOG_DIR = os.path.expanduser("~")

LOGGER_NAME = 'service'
ANALYTICS_LOGGER_NAME = 'analytics'
LOG_DIR = os.path.expanduser("~")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(thread)d %(env)s %(service)s %(handler)s %(requestId)s '
                      '%(message)s'
        },
        'analytics': {
            'format': '%(asctime)s %(env)s %(service)s %(handler)s %(app)s %(account)s %(user)s %(device)s'
        }
    },
    'handlers': {
        'local_internal': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'prjname_service.log'),
            'formatter': 'verbose'
        },
        'local_analytics': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'prjname_analytics.log'),
            'formatter': 'analytics'
        },
    },
    'loggers': {
        LOGGER_NAME: {
            'handlers': ['local_internal'],
            'level': 'DEBUG',
            'propagate': True,
        },
        ANALYTICS_LOGGER_NAME: {
            'handlers': ['local_analytics'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

