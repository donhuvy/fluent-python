from math import hypot

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(self.x or self.y)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__ == "__main__":
    a = Vector(1, 2)
    b = Vector(2, 2)
    c = a + b
    print(c)
    print(abs(c))
    print(c * 10)
    assert bool(c) is True