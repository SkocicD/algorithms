import math
from typing import List
# from fractions import Fraction

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

class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# class to store a line object
# uses form ax + by = c
class line2():
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

    def perp(self, p:p):
        perpline = line2()
        perpline.a = -self.b
        perpline.b = self.a
        perpline.c = perpline.a * p.x + perpline.b * p.y
        return perpline

    def on(self, p:p):
        try:
            return self.a * p.x + self.b * p.y == self.c
        except TypeError:
            return self.a * p.x.numerator * p.y.denominator + self.b * p.y.numerator * p.x.denominator == self.c * p.x.denominator * p.y.denominator
    
    def intersect(self, line):
        # determinant
        det = self.a * line.b - self.b * line.a
        # determinant = 0 either means infinite or no intersections
        if det == 0:
            if self.a == 0 or self.b == 0:
                return self.c == line.c
            # one equation will be some multiple of the other
            return max(self.c, line.c) * min(self.a, line.a) == max(self.a, line.a) * min(self.c, line.c)
        else:
            factor = Fraction(1, det)
            x = line.b * self.c - self.b * line.c
            y = - line.a * self.c + self.a * line.c
            point = p(Fraction(x, det), Fraction(y,det))
            return point

    def same_side(self, p1:p, p2:p):
        if self.on(p1) or self.on(p2):
            return True
        return (self.a * p1.x + self.b * p1.y < self.c) == (self.a * p2.x + self.b * p2.y < self.c)
    
    def __str__(self):
        return f"{self.a}x + {self.b}y = {self.c}"

# class to store a line segment defined by two points.
# subclass of line
class line_segment(line2):

    # stores the minimum and maximum x and y values, essentially creating a rectangle
    # also keeps a value of length
    def __init__(self, p1:p=None, p2:p=None):
        super().__init__(p1, p2)
        if p1 is not None and p2 is not None:
            self.lengthsq = p1.distancesq(p2)
            self.minx = min(p1.x, p2.x)
            self.maxx = max(p1.x, p2.x)
            self.miny = min(p1.y, p2.y)
            self.maxy = max(p1.y, p2.y)
    
    # overrides on from line. Tells whether a point sits on a line segment
    def on(self, p:p):
        # first sees if the line is on the line in general, if not return false
        if not super().on(p):
            return False
        # otherwise see if it falls within the rectangle created by the line segment, if so, it is on the segment
        # bump the bounds up a little in case floating point problems have occurred
        try:
            return (p.x >= self.minx and p.x <= self.maxx) and (p.y >= self.miny and p.y <= self.maxy)
        except:
            if p.x.denominator < 0:
                p.x.denominator*=-1
                p.x.numerator*=-1
            if p.y.denominator < 0:
                p.y.denominator*=-1
                p.y.numerator*=-1
            return (p.x.numerator >= self.minx * p.x.denominator and p.x.numerator <= self.maxx * p.x.denominator) and \
                    (p.y.numerator >= self.miny * p.y.denominator and p.y.numerator <= self.maxy * p.y.denominator)

    # checks if this segment intersects a line
    def intersect_line(self, line):
        # if the lines dont intersect, then the segment has no chance of hitting the line
        # if one is continuous and they overlap, then they definitely intersect
        p = super().intersect(line)
        if p == False or p == True:
            return p
        else:
            # if the point is on the current segment, return p, otherwise return false
            if self.on(p):
                return p
            else:
                return False
    
    # checks if two line segments overlap
    def intersect_segment(self, seg):
        p = super().intersect(seg)
        # check of lines intersect. If they dont, segments dont either so return false
        if p == False:
            return False
        else:
            # if lines do overlap, see if they overlap within these segments
            if p == True:
                if (self.minx <= seg.minx and seg.minx <= self.maxx) or (seg.minx <= self.minx and self.minx <= seg.maxx):
                    if (self.miny <= seg.miny and seg.miny <= self.maxy) or (seg.miny <= self.miny and self.miny <= seg.maxy):
                        return True
            # otherwise check if the intersection point is on both line segments, if so return that point
            if self.on(p) and seg.on(p):
                return p
            else:
                return False

class pirate():
    def __init__(self, p1:p, p2:p):
        self.stand = p1
        self.look = p2
        self.radius = line_segment(self.stand, self.look)
        self.treasureline = line_segment(self.stand, treasure)
        self.perpline = self.radius.perp(self.stand)
        self.can_see = True
    
    def __str__(self):
        return f"Pirate[{self.stand}, {self.look}]"


if __name__ == '__main__':
    # get wall count and pirate count
    wall_c, pirate_c = input().split()
    wall_c = int(wall_c)
    pirate_c = int(pirate_c)

    # get treasure coordinates
    x, y = input().split()
    treasure = p(int(x), int(y))

    # fill lists of walls and pirates
    walls:List[line_segment] = []
    pirates:List[pirate] = []
    for _ in range(wall_c):
        x1, y1, x2, y2 = [int(z) for z in input().split()]
        walls.append(line_segment(p(x1, y1), p(x2, y2)))
    for _ in range(pirate_c):
        x1, y1, x2, y2 = [int(z) for z in input().split()]
        pirates.append(pirate(p(x1, y1), p(x2, y2)))

    # start by checking which points are within range of the treasure
    for pir in pirates:
        # remove pirate it doesnt have enough range
        if pir.radius.lengthsq < pir.treasureline.lengthsq:
            pir.can_see = False
            print("not visible")
            continue
        # remove pirate if it is looking in the wrong direction
        if not pir.perpline.same_side(pir.look, treasure):
            pir.can_see = False
            print("not visible")
            continue
        # remove pirate if any of the walls intersect with the pirates view of the treasure
        for wall in walls:
            intersection = pir.treasureline.intersect_segment(wall)
            if intersection != False:
                pir.can_see = False
                print("not visible")
                break
        if not pir.can_see:
            continue
        # remove pirate if any other pirates are in the path from the pirate to the treasure
        for pir2 in pirates:
            if pir != pir2 and pir.treasureline.on(pir2.stand):
                pir.can_see = False
                print("not visible")
                break
        if not pir.can_see:
            continue
        # if it wasnt removed print visible
        print("visible")
