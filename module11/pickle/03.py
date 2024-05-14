from __future__ import annotations

from pickle import dumps
from pickle import loads


class A:
    x = "some"

    def __init__(self):
        print("new A!")
        self.y = "Another variable"


a = A()
ser = dumps(a)
ser_class = dumps(A)

print(ser)
restored_a = loads(ser)
restored_A = loads(ser_class)
print(restored_a.y)
print(a == restored_a)
print(A == restored_A)
