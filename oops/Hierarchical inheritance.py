class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side * self.side

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

c1 = Circle(5)
c2=Square(4)
print(c1.area())
print(c2.area())
