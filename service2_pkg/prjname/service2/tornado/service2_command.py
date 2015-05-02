from prjname.common.tornado.start_service_command import StartServiceCommand
from prjname.service2.tornado.application import APPLICATION


class Service2Command(StartServiceCommand):  # pylint: disable=too-few-public-methods
    DEFAULT_PORT = 10002

    def __init__(self, app, app_args):
        super(Service2Command, self).__init__(app, app_args, APPLICATION)

    def get_description(self):
        return "service2 service"
