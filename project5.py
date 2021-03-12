# CI SHI
# 2020/03/11


import math
import numpy as np

class Shape(object):
    def __init__(self,EdgeLength,EdgeNum):
        self.EdgeLength = EdgeLength
        self.EdgeNum = EdgeNum
    def __str__(self):
        if self.EdgeNum == 1:
            return "create a Regular circle"
        elif self.EdgeNum == 3:
            return "create a Regular triangle"
        elif self.EdgeNum == 4:
            return "create a Regular quadrilateral"
        elif self.EdgeNum > 4:
            return "create a Regular polygon"
    def perimeter(self):
        return self.EdgeLength * self.EdgeNum
    def area(self):
        return "The area formula based on thype of shape, we will list different formula that corresponding to different shape\n" \
               "In class Shape, we assume all shape are Regular Geometic Shape"

class Rectangle(object):
    def __init__(self,Baseline,Heightline):
        self.Baseline = Baseline
        self.Hightline = Heightline
    def perimeter(self):
        return (self.Baseline * 2) + (self.Hightline * 2)
    def area(self):
        return self.Baseline * self.Hightline
    def diagonal(self):
        return math.sqrt((self.Baseline ** 2) + (self.Hightline ** 2))

class Oval(object):
    def __init__(self, majoradius,minoradius):
        self.majoradius = majoradius
        self.minoradius = minoradius
    def perimeter(self):
        if int(self.majoradius)>int(self.minoradius):
            return 2 * self.minoradius * math.pi + 4 * (self.majoradius-self.minoradius)
        else:
            return "The Length of majoradius is bigger than length of minoradius"
    def area(self):
        if int(self.majoradius)>int(self.minoradius):
            return math.pi * self.majoradius * self.minoradius
        else:
            return "The Length of majoradius is bigger than length of minoradius"

class Polypon(object):
    def __init__(self,side):
        self.side = side
    def perimeter(self):
        return sum(self.side)
    def area(self):
        n= len (self.side)
        area = 0
        for point in range(n):
            area += self.side[point-1][0]*self.side[point][1]
            area -= self.side[point-1][1]*self.side[point][0]
        area = abs(area)/2
        return area
    # the area function work depended on the principle of the Shoelace Formula.
    # It can calculate the area of the polygon (also include irregular polygons) by coordinates

a = np.array([(1,5),(3,7),(2,4),(6,8),(3,6)])
b = Polypon(a)
c = b.area()
print(c)

class Square(object):
    def __init__(self,sidelength):
        self.sidelength = sidelength
    def perimeter(self):
        return self.sidelength * 4
    def area(self):
        return self.sidelength ** 2
    def diagonal(self):
        return math.sqrt(2*(self.sidelength**2))

class Triangle(object):
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    def area(self):
        p = (Triangle.perimeter(self)/2)
        a = (p-self.side1)
        b = (p-self.side2)
        c = (p-self.side3)
        return math.sqrt(p*a*b*c)

a = Triangle(3,4,5)
b = a.area()

class Pentagon(object):
    def __init__(self,side):
        self.side = side
    def diagonal(self):
        return ((1+math.sqrt(5))/2)*self.side
    def perimeter(self):
        return self.side * 5
    def area(self):
        area = ((math.sqrt(5*(5+2*math.sqrt(5))))*(self.side**2))/4
        return area

a = Pentagon(5)
b = a.area()

class Circle(object):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius**2)
    def diameter(self):
        return self.radius*2
    def perimter(self):
        return 2*math.pi*self.radius


class Parallelogram(object):
    def __init__(self,baseside,obliqueside,obtuseangle,actuteangle):
        self.baseside = baseside
        self.obliqueside = obliqueside
        self.obtuseangle = obtuseangle
        self.actuteangle = actuteangle
    def diagonal1(self):
        if self.obtuseangle < 180 and self.obtuseangle > 90 and (self.obtuseangle + self.actuteangle) == 180:
            return math.sqrt((self.baseside**2)+(self.obliqueside**2)-2*(self.baseside * self.obliqueside)*math.cos(self.obtuseangle))
        else:
            return "the angle that you entered was wrong"
    def diagonal2(self):
        if self.actuteangle < 90 and self.actuteangle > 0 and (self.obtuseangle + self.actuteangle) == 180:
            return math.sqrt((self.baseside**2)+(self.obliqueside**2)-2*(self.baseside * self.obliqueside)*math.cos(self.actuteangle))
        else:
            return "the angle that you entered was wrong"
    def perimter(self):
        d1 = Parallelogram.diagonal1(self)
        d2 = Parallelogram.diagonal2(self)
        return 2 * self.baseside + math.sqrt(2*(d1**2)+2*(d2**2)-4*(self.obliqueside**2))
    def area(self):
        return self.baseside*self.obliqueside*math.sin(self.obtuseangle)


class Rhombus(object):
    def __init__(self,side,angle1,angle2):
        self.side = side
        self.angle1 = angle1
        self.angle2 = angle2
    def diagonal1(self):
        if self.angle1 + self.angle2 == 180:
             return self.side * math.sqrt(2+2*math.cos(self.angle1))
        else:
             return "the angle that you entered was wrong"

    def diagonal2(self):
        if self.angle1 + self.angle2 == 180:
            return self.side * math.sqrt(2-2*math.cos(self.angle1))
        else:
            return "the angle that you entered was wrong"
    def perimter(self):
        return self.side * 4
    def area(self):
       d1 = Rhombus.diagonal1(self)
       d2 = Rhombus.diagonal2(self)
       return (d1*d2)/2



