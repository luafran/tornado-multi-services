"""
Base settings used in all environments
"""
import collections
import datetime
import os

AUTO_RELOAD = False

APPLICATION_ID = '1'

JSON_SCHEMA_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'json_schema', 'schemas')
JSON_SCHEMA_BASE_URL = "http://prjname/jsonschema/"

JWT_TOKEN_NOT_BEFORE_TIMEDELTA = datetime.timedelta(minutes=1)

DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

ENFORCE_POLICIES = True

