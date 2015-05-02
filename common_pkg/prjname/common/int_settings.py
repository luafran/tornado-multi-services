"""
Settings used in development environments
"""
import os

ENVIRONMENT_NAME = 'INT'

STATS_ENABLED = False
STATS_SERVICE_HOSTNAME = '54.164.227.227'

LOG_DIR = '/var/log/prjname'

LOGGER_NAME = 'service'
ANALYTICS_LOGGER_NAME = 'analytics'
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
