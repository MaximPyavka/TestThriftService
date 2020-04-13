from thrift.Thrift import TType

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None


class Vector:
    """
    Attributes:
     - x
     - y
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I16, 'x', None, None,),  # 1
        (2, TType.I16, 'y', None, None,),  # 2
    )

    def __init__(self, x=None, y=None, ):
        self.x = x
        self.y = y

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans,
                                                                                        TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I16:
                    self.x = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.y = iprot.readI16()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Vector')
        if self.x is not None:
            oprot.writeFieldBegin('x', TType.I16, 1)
            oprot.writeI16(self.x)
            oprot.writeFieldEnd()
        if self.y is not None:
            oprot.writeFieldBegin('y', TType.I16, 2)
            oprot.writeI16(self.y)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        l = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(l))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
