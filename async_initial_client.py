from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from async_service.factorial import FactorialOperation
from config import server_ip, init_tcp


def main():
    transport = TSocket.TSocket(server_ip, init_tcp)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = FactorialOperation.Client(protocol)

    transport.open()
    print("---- Opened transport socket for client ----")

    for i in range(11, 21):
        client.factorial_init(20)

    transport.close()
    print("---- Closed transport socket for client ----")


if __name__ == '__main__':
    main()
