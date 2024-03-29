import time
import logging

from dirt import DirtApp, runloop

log = logging.getLogger(__name__)

class FirstMock(object):
    def ping(self):
        log.info("mock got ping...")
        return "mock pong"

class FirstAPI(object):
    def ping(self):
        log.info("got ping...")
        return "pong"

class FirstApp(DirtApp):
    def get_api(self, edge, call):
        return FirstAPI()

    def start(self):
        log.info("starting...")


class SecondApp(DirtApp):
    @runloop(log)
    def serve(self):
        log.info("Trying to ping FirstApp...")
        api_zrpc = self.settings.get_api("first_zrpc")
        api_drpc = self.settings.get_api("first_drpc")
        while True:
            log.info("ping zrpc: %r", api_zrpc.ping())
            log.info("ping drpc: %r", api_drpc.ping())
            time.sleep(1)
