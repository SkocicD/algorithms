from fractions import Fraction
import math

# Class to store a point object, (x, y)
class p():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # finds the pistance between the current point and p2
    def distancesq(self, p2):
        return (self.x-p2.x)**2 + (self.y-p2.y)**2

    def __str__(self):
        return f"({self.x}, {self.y})"

# class to store a line object
# uses form ax + by = c
class line():
    # create a line object based on two points that it passes through
    # stores the slope and y-intercept, or if it is vertical or horizontal, stores its respective x or y value
    def __init__(self, p1:p=None, p2:p=None):
        if p1 is not None and p2 is not None:
            # same x means vertical line
            if p1.x == p2.x:
                self.a = 1
                self.b = 0
                self.c = p1.x
            # same y means horizontal line
            elif p1.y == p2.y:
                self.a = 0
                self.b = 1
                self.c = p1.y
            # neither vertical or horizontal
            else:
                # slope
                m = Fraction(p1.y-p2.y, p1.x-p2.x)
                self.a = -m.numerator
                self.b = m.denominator
                self.c = self.a * p1.x + self.b * p1.y

    def on(self, p:p):
        return self.a * p.x + self.b * p.y == self.c
    
    def intersect(self, line):
        # determinant
        det = self.a * line.b - self.b * line.a
        # determinant = 0 either means infinite or no intersections
        if det == 0:
            if self.a == 0 or self.b == 0:
                return self.c == line.c
            # one equation will be some multiple of the other
            return self.c * line.a == self.a * line.c
        else:
            x = line.b * self.c - self.b * line.c
            y = - line.a * self.c + self.a * line.c
            point = p(Fraction(x, det), Fraction(y,det))
            if point.x < -1000000000 or point.x > 1000000000 or point.y < -1000000000 or point.y > 1000000000:
                return False
            return point
    
    def __str__(self):
        return f"{self.a}x + {self.b}y = {self.c}"

class triangle:
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3

        self.minx=min(self.p1.x,self.p2.x,self.p3.x)
        self.miny=min(self.p1.y,self.p2.y,self.p3.y)
        self.maxx=max(self.p1.x,self.p2.x,self.p3.x)
        self.maxy=max(self.p1.y,self.p2.y,self.p3.y)
        self.bounding_rect=rectangle(p(self.minx,self.miny),p(self.maxx,self.maxy))

    def divide_bounding_rectangle(self):
        # break into 3 triangles...
        # some of these triangles will have two duplicate points
        # this means they have 0 area, but the intArea is nonzero
        # also there will be a "fourth" triangle that is just a point
        # this also has an intArea of 1 assuming its on a discrete point not somewhere in space.

        self.rtri=[]
        # get the triangle that is the top leftmost point of this triangle,bottom leftmost point, and top leftmost point of bounding rect
        ps=[self.p1,self.p2,self.p3]
        tmp=[]
        for pt in ps:
            if pt.x==self.minx
                tmp.append(pt)

        

class rectangle:
    # defined by two opposite corners
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        self.p3=p(p1.x,p2.y)
        self.p4=p(p2.x,p1.y)

    def inclusiveIntArea(self):
        (math.floor(max(self.p1.x,self.p2.x))-math.ceil(min(self.p1.x,self.p2.x))+1)*(math.floor(max(self.p1.y,self.p2.y))-math.ceil(min(self.p1.y,self.p2.y))+1)

n=int(input())
ps=[]
lines=[]
for _ in range(n):
    ps.append(p(*list(map(int,input().split()))))
for i in range(n):
    lines.append(line(ps[i-1],ps[i]))

for i in range(n):
    print(lines[i-2].intersect(lines[i]),end=', ')
    print(f'{ps[i-2]}, {ps[i-1]}')
