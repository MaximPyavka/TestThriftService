namespace py Factorial

service FactorialOperation {
    void factorial_init(1: i16 n)
}

service FactorialResults {
     void factorial_res(1: i64 n)
}