import math

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from vector.ttypes import Vector
from matrix import MatrixOperations
from config import server_ip, server_tcp


def main():
    transport = TSocket.TSocket(server_ip, server_tcp)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = MatrixOperations.Client(protocol)

    transport.open()
    print("---- Opened transport socket for client ----")

    print("---- Testing Dot Product ----")
    v1 = Vector(2, 3)
    v2 = Vector(4, 5)

    dp = client.dot_product(v1, v2)
    assert v1.x * v2.x + v1.y * v2.y == dp

    print("---- Testing Length ----")
    len1 = client.length(v1)
    len2 = client.length(v2)
    assert len1 == (v1.x * v1.x + v1.y * v1.y) ** 0.5
    assert len2 == (v2.x * v2.x + v2.y * v2.y) ** 0.5

    print("---- Testing Cosine & Angle ----")
    cos = client.cos(v1, v2)
    angle = client.angle(v1, v2)
    assert cos == dp / (len1 * len2)
    assert angle == math.acos(dp / (len1 * len2))

    print("---- Testing Is Angle Right ----")
    ira1 = client.is_angle_right(Vector(2, 0), Vector(0, 2))  # True
    ira2 = client.is_angle_right(Vector(4, 1), Vector(-1, 4))  # True
    assert ira1 and ira2
    assert not client.is_angle_right(v1, v2)  # False

    print("---- Testing Matrix Multiplication ----")
    m1 = [[4, 8], [0, 2], [1, 6]]
    m2 = [[5, 2], [9, 4]]
    m_dot = client.multiply_matrix(m1, m2)
    assert m_dot == [[92, 40], [18, 8], [59, 26]]

    print("---- Testing Matrix Transpose ----")
    m_trans = client.transpose_matrix(m1)
    assert m_trans == [[4, 0, 1], [8, 2, 6]]

    transport.close()
    print("---- Closed transport socket for client ----")


if __name__ == '__main__':
    main()
