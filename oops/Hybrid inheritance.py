class A:
    def a(self): return "A"

class B(A):
    def b(self): return "B"

class C(A):
    def c(self): return "C"

class D(B, C): 
    pass
c1 = D()
print(c1.a(), c1.b(), c1.c())