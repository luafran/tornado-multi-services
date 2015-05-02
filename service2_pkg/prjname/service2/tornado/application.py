"""
Application definitions and URL mappings
"""
from tornado import web

from prjname.service2 import settings
from prjname.common.tornado.handlers import health


APPLICATION = web.Application(
    [
        (r'.*/health/?$', health.HealthHandler,
         {'application_settings': settings, 'handler': 'Health'})
    ],
    service_name='service2',
    autoreload=settings.AUTO_RELOAD)
