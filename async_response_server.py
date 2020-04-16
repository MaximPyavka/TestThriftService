import sys
import logging
from logging import config

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


from server import logging_method, BaseHandler
from config import server_ip, resp_tcp
from async_service.factorial import FactorialResults
from config import logging_conf

logger = logging.getLogger('async_response_server')
config.dictConfig(logging_conf)


class DB:
    def __init__(self):
        self._db = {}

    def insert(self, n):
        self._db[len(self._db) + 1] = n

    def count(self):
        return len(self._db)

    def select_all(self):
        return self._db


fake_db = DB()


class FactorialResultsServerHandler(BaseHandler):

    @logging_method(logger)
    def factorial_res(self, n):
        fake_db.insert(n)


if __name__ == '__main__':
    processor = FactorialResults.Processor(FactorialResultsServerHandler())
    transport = TSocket.TServerSocket(server_ip, resp_tcp)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    try:
        logger.info("----Starting Thrift Server Process at {0}:{1}----".format(server_ip, resp_tcp))
        server.serve()
    except KeyboardInterrupt:
        logger.info("----User closes Server Process at {0}:{1}----".format(server_ip, resp_tcp))
    except BaseException as e:
        logger.critical(f"----Unfortunately closed Server Process at {server_ip}:{resp_tcp}"
                        f"with {sys.exc_info()[0]}----")
    logger.info(f"----Items in db - {fake_db.count()}----")
