# *Для рассмотренного на уроке класса Circle реализовать метод производящий
# вычитание двух окружностей, вычитание радиусов произвести по модулю.
# Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.

import math
from task_01 import Point


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return super().__str__() + f', radius={self.radius})'

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = self.radius - other.radius
        return Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)


m = Circle(25, 9, 13)
n = Circle(8)
l = Circle(30, 13, 17)

print(m == n)
print(m == l)

z = m - l

print(m)
print(n)
print(l)
print(z)
