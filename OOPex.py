print("\nQuestion 1")

class Apple():
    def __init__(self, b, c, p, a):
        print("Apple object instantiated!")
        self.brand = b
        self.color = c
        self.cost = p
        self.aging = a       

apple=Apple(1,2,3,4)

print("\nQuestion 2")

import math
class Circle():
    def __init__(self):
        radius=int(input("Enter a radius:"))
        self.r = radius
        self.pi = math.pi

    def area(self):
        return self.pi*self.r**2

circle=Circle()
print("Area = " + str(circle.area()))
        
print("\nQuestion 3")

class Triangle():
    def __init__(self, tbase):
        self.b = tbase
        self.h = 3
        
    def area(self):
        """ Returns 1/2(b*h).
        :param b: float.
        :param h: flotat.
        :return: float product of 1/2(base*height). """
        
        return 1/2*self.b*self.h

base = float(input("Enter triangle's base:"))
triangle = Triangle(base)
print("Area of triangle = " + str(triangle.area()))

#############################
print("\nQuestion 4")

class Hexagon():
    def __init__(self, ax, bx, cx, dx, ex, fx):
        self.side1 = ax
        self.side2 = bx
        self.side3 = cx
        self.side4 = dx
        self.side5 = ex
        self.side6 = fx
        self.perimeter = 0
        self.sides = []

    def calculate_perimeter(self):
        return self.side1+self.side2+self.side3+self.side4+self.side5+self.side6

hexagon=Hexagon(2,2,2,2,2,2)
print("Hexagon:Sum of six sides=" + str(hexagon.calculate_perimeter()))

     #####################################
