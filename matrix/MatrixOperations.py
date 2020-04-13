#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from vector import VectorOperations
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol

try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None


class Iface(VectorOperations.Iface):
    def multiply_matrix(self, matrix1, matrix2):
        """
        Parameters:
         - matrix1
         - matrix2
        """
        pass

    def transpose_matrix(self, matrix):
        """
        Parameters:
         - matrix
        """
        pass


class Client(VectorOperations.Client, Iface):
    def __init__(self, iprot, oprot=None):
        VectorOperations.Client.__init__(self, iprot, oprot)

    def multiply_matrix(self, matrix1, matrix2):
        """
        Parameters:
         - matrix1
         - matrix2
        """
        self.send_multiply_matrix(matrix1, matrix2)
        return self.recv_multiply_matrix()

    def send_multiply_matrix(self, matrix1, matrix2):
        self._oprot.writeMessageBegin('multiply_matrix', TMessageType.CALL, self._seqid)
        args = multiply_matrix_args()
        args.matrix1 = matrix1
        args.matrix2 = matrix2
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_multiply_matrix(self):
        (fname, mtype, rseqid) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = multiply_matrix_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "multiply_matrix failed: unknown result");

    def transpose_matrix(self, matrix):
        """
        Parameters:
         - matrix
        """
        self.send_transpose_matrix(matrix)
        return self.recv_transpose_matrix()

    def send_transpose_matrix(self, matrix):
        self._oprot.writeMessageBegin('transpose_matrix', TMessageType.CALL, self._seqid)
        args = transpose_matrix_args()
        args.matrix = matrix
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_transpose_matrix(self):
        (fname, mtype, rseqid) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = transpose_matrix_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "transpose_matrix failed: unknown result");


class Processor(VectorOperations.Processor, Iface, TProcessor):
    def __init__(self, handler):
        VectorOperations.Processor.__init__(self, handler)
        self._processMap["multiply_matrix"] = Processor.process_multiply_matrix
        self._processMap["transpose_matrix"] = Processor.process_transpose_matrix

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_multiply_matrix(self, seqid, iprot, oprot):
        args = multiply_matrix_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = multiply_matrix_result()
        result.success = self._handler.multiply_matrix(args.matrix1, args.matrix2)
        oprot.writeMessageBegin("multiply_matrix", TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_transpose_matrix(self, seqid, iprot, oprot):
        args = transpose_matrix_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = transpose_matrix_result()
        result.success = self._handler.transpose_matrix(args.matrix)
        oprot.writeMessageBegin("transpose_matrix", TMessageType.REPLY, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class multiply_matrix_args:
    """
    Attributes:
     - matrix1
     - matrix2
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'matrix1', (TType.LIST, (TType.I16, None)), None,),  # 1
        (2, TType.LIST, 'matrix2', (TType.LIST, (TType.I16, None)), None,),  # 2
    )

    def __init__(self, matrix1=None, matrix2=None, ):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

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
                if ftype == TType.LIST:
                    self.matrix1 = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = []
                        (_etype9, _size6) = iprot.readListBegin()
                        for _i10 in range(_size6):
                            _elem11 = iprot.readI16();
                            _elem5.append(_elem11)
                        iprot.readListEnd()
                        self.matrix1.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.matrix2 = []
                    (_etype15, _size12) = iprot.readListBegin()
                    for _i16 in range(_size12):
                        _elem17 = []
                        (_etype21, _size18) = iprot.readListBegin()
                        for _i22 in range(_size18):
                            _elem23 = iprot.readI16();
                            _elem17.append(_elem23)
                        iprot.readListEnd()
                        self.matrix2.append(_elem17)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('multiply_matrix_args')
        if self.matrix1 is not None:
            oprot.writeFieldBegin('matrix1', TType.LIST, 1)
            oprot.writeListBegin(TType.LIST, len(self.matrix1))
            for iter24 in self.matrix1:
                oprot.writeListBegin(TType.I16, len(iter24))
                for iter25 in iter24:
                    oprot.writeI16(iter25)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.matrix2 is not None:
            oprot.writeFieldBegin('matrix2', TType.LIST, 2)
            oprot.writeListBegin(TType.LIST, len(self.matrix2))
            for iter26 in self.matrix2:
                oprot.writeListBegin(TType.I16, len(iter26))
                for iter27 in iter26:
                    oprot.writeI16(iter27)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class multiply_matrix_result:
    """
    Attributes:
     - success
    """

    thrift_spec = (
        (0, TType.LIST, 'success', (TType.LIST, (TType.I16, None)), None,),  # 0
    )

    def __init__(self, success=None, ):
        self.success = success

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
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype31, _size28) = iprot.readListBegin()
                    for _i32 in range(_size28):
                        _elem33 = []
                        (_etype37, _size34) = iprot.readListBegin()
                        for _i38 in range(_size34):
                            _elem39 = iprot.readI16();
                            _elem33.append(_elem39)
                        iprot.readListEnd()
                        self.success.append(_elem33)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('multiply_matrix_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.LIST, len(self.success))
            for iter40 in self.success:
                oprot.writeListBegin(TType.I16, len(iter40))
                for iter41 in iter40:
                    oprot.writeI16(iter41)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class transpose_matrix_args:
    """
    Attributes:
     - matrix
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'matrix', (TType.LIST, (TType.I16, None)), None,),  # 1
    )

    def __init__(self, matrix=None, ):
        self.matrix = matrix

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
                if ftype == TType.LIST:
                    self.matrix = []
                    (_etype45, _size42) = iprot.readListBegin()
                    for _i46 in range(_size42):
                        _elem47 = []
                        (_etype51, _size48) = iprot.readListBegin()
                        for _i52 in range(_size48):
                            _elem53 = iprot.readI16();
                            _elem47.append(_elem53)
                        iprot.readListEnd()
                        self.matrix.append(_elem47)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('transpose_matrix_args')
        if self.matrix is not None:
            oprot.writeFieldBegin('matrix', TType.LIST, 1)
            oprot.writeListBegin(TType.LIST, len(self.matrix))
            for iter54 in self.matrix:
                oprot.writeListBegin(TType.I16, len(iter54))
                for iter55 in iter54:
                    oprot.writeI16(iter55)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class transpose_matrix_result:
    """
    Attributes:
     - success
    """

    thrift_spec = (
        (0, TType.LIST, 'success', (TType.LIST, (TType.I16, None)), None,),  # 0
    )

    def __init__(self, success=None, ):
        self.success = success

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
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype59, _size56) = iprot.readListBegin()
                    for _i60 in range(_size56):
                        _elem61 = []
                        (_etype65, _size62) = iprot.readListBegin()
                        for _i66 in range(_size62):
                            _elem67 = iprot.readI16();
                            _elem61.append(_elem67)
                        iprot.readListEnd()
                        self.success.append(_elem61)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('transpose_matrix_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.LIST, len(self.success))
            for iter68 in self.success:
                oprot.writeListBegin(TType.I16, len(iter68))
                for iter69 in iter68:
                    oprot.writeI16(iter69)
                oprot.writeListEnd()
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)