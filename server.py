import sys
import math
import random
import logging

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from matrix import MatrixOperations
from config import server_ip, server_tcp, logging_conf

from logging import config

terminal_logger = logging.getLogger('terminal')
file_logger = logging.getLogger('idl_service')

config.dictConfig(logging_conf)


def logging_method(method):
    def wrapper(self, *args, **kwargs):
        unique_hash = str(random.getrandbits(64))
        # TODO add Queue logging handler for asynchronous logging
        mes_beg = f'{unique_hash} - For method {method.__name__}'
        mes = mes_beg + f' - got positional arguments: {args} and key-word arguments: {kwargs}'
        file_logger.info(mes)
        res = method(self, *args, **kwargs)
        mes2 = mes_beg + f' - got result: {res}'
        file_logger.debug(mes2)
        return res
    return wrapper


class BaseHandler:
    def __init__(self):
        self.log = {}


class VectorOperationsHandler(BaseHandler):
    @logging_method
    def dot_product(self, vector1, vector2):
        return vector1.x * vector2.x + vector1.y * vector2.y

    @logging_method
    def length(self, vector1):
        return math.sqrt(vector1.x * vector1.x + vector1.y * vector1.y)

    @logging_method
    def cos(self, vector1, vector2):
        return self.dot_product(vector1, vector2) / (self.length(vector1) * self.length(vector2))

    @logging_method
    def angle(self, vector1, vector2):
        return math.acos(self.cos(vector1, vector2))

    @logging_method
    def is_angle_right(self, vector1, vector2):
        return self.cos(vector1, vector2) == 0

    @staticmethod
    def is_null_vector(vector1):
        return vector1.x == 0 and vector1 == 0


class MatrixOperationHandler(VectorOperationsHandler):
    def multiply_matrix(self, m1, m2):
        res_rows = self.get_number_of_rows(m2)
        res = []
        for n, i in enumerate(m1):
            res.append([])
            for m in range(res_rows):
                cell = 0
                for e, j in enumerate(m2):
                    cell += i[e]*j[m]
                res[n].append(cell)
        return res

    def transpose_matrix(self, m1):
        return [[r[i] for r in m1] for i in range(self.get_number_of_columns(m1))]

    @staticmethod
    def get_number_of_rows(matrix):
        return len(matrix)

    @staticmethod
    def get_number_of_columns(matrix):
        return len(matrix[0])


if __name__ == '__main__':
    processor = MatrixOperations.Processor(MatrixOperationHandler())
    transport = TSocket.TServerSocket(server_ip, server_tcp)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    server.setNumThreads(5)
    try:
        terminal_logger.info("----Starting Thrift Server Process at {0}:{1}----".format(server_ip, server_tcp))
        server.serve()
    except KeyboardInterrupt:
        terminal_logger.info("----User closes Server Process at {0}:{1}----")
    except BaseException as e:
        terminal_logger.critical(f"----Unfortunately closed Server Process at {0}:{1} with {sys.exc_info()[0]}----")
