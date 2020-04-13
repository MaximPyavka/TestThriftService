include "vector.thrift"

namespace py matrix

service MatrixOperations extends vector.VectorOperations{
    list<list<i16>> multiply_matrix(1: list<list<i16>> matrix1, 2: list<list<i16>> matrix2)
    list<list<i16>> transpose_matrix(1: list<list<i16>> matrix)
}