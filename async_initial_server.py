import sys
import logging
from multiprocessing import Queue, Process
from queue import Full
from logging import config

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


from server import logging_method, BaseHandler
from config import server_ip, init_tcp, resp_tcp
from async_service.factorial import FactorialOperation
from async_response_client import ResponseClientProcess
from config import logging_conf


logger = logging.getLogger('async_initial_server')
config.dictConfig(logging_conf)


class FactorialInitialServerHandler(BaseHandler):
    def __init__(self, queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue_for_response = queue

    @logging_method(logger)
    def factorial_init(self, n):
        try:
            self.queue_for_response.put_nowait(n)
        except Full:
            return

class TChainedThreadPoolServer(TServer.TThreadPoolServer):
    def start_response_client_process(self, server_ip, resp_tcp, queue):
        p = Process(target=ResponseClientProcess.start_response_process_client, args=(server_ip, resp_tcp, queue))
        p.start()


if __name__ == '__main__':
    queue = Queue()
    processor = FactorialOperation.Processor(FactorialInitialServerHandler(queue))
    transport = TSocket.TServerSocket(server_ip, init_tcp)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TChainedThreadPoolServer(processor, transport, tfactory, pfactory)
    server.start_response_client_process(server_ip, resp_tcp, queue)
    server.setNumThreads(5)
    try:
        logger.info("----Starting Thrift Server Process at {0}:{1}----".format(server_ip, init_tcp))
        server.serve()
    except KeyboardInterrupt:
        logger.info("----User closes Server Process at {0}:{1}----")
    except BaseException as e:
        logger.critical(f"----Unfortunately closed Server Process at {server_ip}:{init_tcp}"
                        f" with {sys.exc_info()[0]}----")
