import clr

clr.AddReference('kokokotest')

from HelloApp import Program

if __name__ == '__main__':
    print("Calculating greatest common divisor")
    p = Program()
    assert p.gcd(111111111, 123456789) == 9
