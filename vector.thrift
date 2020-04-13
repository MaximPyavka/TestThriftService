namespace py Vector

struct Vector {
    1: i16 x
    2: i16 y
}

service VectorOperations {
    i16 dot_product(1: Vector v, 2: Vector u)
    double length(1: Vector v)
    double cos(1: Vector v, 2: Vector u)
    double angle(1: Vector v, 2: Vector u)
    bool is_angle_right(1: Vector v, 2: Vector u)
}

service Matrix {
    list<list<i16>> MultiplyMatrix(1: list<list<i16>> matrix)
    list<list<i16>> TransposeMatrix(1: list<list<i16>> matrix)
}