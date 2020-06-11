import math

class trigo:
    # Initializing the side lengths passed to the class
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths
        self.a = side_lengths[0]
        self.b = side_lengths[1]
        self.c = side_lengths[2]
    # Finding the angle type of the triangle or if the sides even equal a triangle
    def find_triangle_type(self):
        if (self.a + self.b) > self.c:
            if self.c**2 == self.a**2 + self.b**2:
                return 'right'
            elif self.c**2 > self.a**2 + self.b**2:
                return 'obtuse'
            elif self.c**2 < self.a**2 + self.b**2:
                return 'acute'
        else:
            return False
    # Finding the type of sides are on the triangle
    def find_triangle(self):
        if self.a == self.b and self.b == self.c:
            return 'equilateral'
        elif self.a == self.b:
            return 'isoceles'
        elif self.a != self.b and self.b != self.c:
            return 'scalene'
    # Finsing the area of the triangle
    def find_area(self):
        self.s = (self.a + self.b + self.c) / 2
        return math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))
    # Finding the perimeter of the triangle
    def perimeter(self):
        return self.a + self.b + self.c
    # Finding all three angles of the triangle according to the side lengths
    def find_angles(self):
        pass