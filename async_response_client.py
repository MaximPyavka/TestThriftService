from queue import Empty

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from async_service.factorial import FactorialResults
from async_service.utils import factorial


class ResponseClientProcess:
    def __init__(self, server_ip, resp_tcp, queue):
        self._transport = TTransport.TBufferedTransport(TSocket.TSocket(server_ip, resp_tcp))
        self._protocol = TBinaryProtocol.TBinaryProtocol(self._transport)
        self._client = FactorialResults.Client(self._protocol)
        self._queue = queue

    @classmethod
    def start_response_process_client(cls, server_ip, resp_tcp, queue):
        client_process = ResponseClientProcess(server_ip, resp_tcp, queue)
        with client_process as client:
            client.run()

    def run(self):
        while self._transport.isOpen():
            try:
                n = self._queue.get_nowait()
            except Empty:
                n = None

            if n is None:
                continue
            self._client.factorial_res(factorial(n))

    def __enter__(self):
        print("---- Opened transport socket for Response  client ----")
        self._transport.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("---- Closed transport socket for Response client ----")
        self._transport.close()
