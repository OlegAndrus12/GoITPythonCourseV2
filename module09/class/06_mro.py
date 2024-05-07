class A:
    x = "a"


class B(A):
    x = "b"


class C(A):
    x = "c"


class D(B, C):
    def get_x(self):
        return D.x


print(D.__mro__)

d = D()
d.get_x()
