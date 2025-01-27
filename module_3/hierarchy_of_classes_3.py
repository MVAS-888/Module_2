class A:
    def method(self):
        print("Method in A")


class B(A):
    def method(self):
        print("Method in B")


class C(A):
    def method(self):
        print("Method in C")


class D(B, C):
    pass


obj = D()
obj.method()

# Вивести порядок вирішення методів
print(D.mro())
