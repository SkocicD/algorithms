import math
from typing import List
from fractions import Fraction

# Class to store a point object, (x, y)
class p():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # finds the pistance between the current point and p2
    def distance(self, p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)

    def __str__(self):
        return f"({self.x}, {self.y})"


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
        return self.a * p.x + self.b * p.y == self.c
    
    def intersect(self, line):
        # determinant
        det = self.a * line.b - self.b * line.a
        # determinant = 0 either means infinite or no intersections
        if det == 0:
            if self.a == 0 or self.b == 0:
                return self.c == line.c
            # one equation will be some multiple of the other
            # use max to keep it a whole number
            factor = max(self.a, line.a) / min(self.a, line.a)
            # return if the equations are the same just scaled, or shifted
            # scaled means infinite (true), shifted means no solutions (false)
            return max(self.c, line.c) == factor * min(self.c, line.c)
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

# class to store a line object
class line():
    # create a line object based on two points that it passes through
    # stores the slope and y-intercept, or if it is vertical or horizontal, stores its respective x or y value
    def __init__(self, p1:p=None, p2:p=None):
        if p1 is not None and p2 is not None:
            # same x means vertical line
            if p1.x == p2.x:
                self.v = True
                self.h = False
                # this equation would be x = something, and something is equal to the x-value of one of the points
                self.x = p1.x
            # same y means horizontal line
            elif p1.y == p2.y:
                self.v = False
                self.h = True
                # this equation would be y = something, and something is equal to the y-value of one of the points
                self.y = p1.y
            # neither vertical or horizontal
            else:
                self.v = False
                self.h = False
                # slope
                self.m = fraction(p1.y-p2.y, p1.x-p2.x)
                # y-intercept
                self.b = p1.y - p1.x * self.m.get()

    # returns the line that is perpendicular through the 
    def perp(self, p:p):
        perpend = line()
        if self.v:
            # perpendicular to vertical is horiz
            perpend.h = True
            perpend.v = False
            # get y from point it passes through
            perpend.y = p.y
        elif self.h:
            #perpendicular to horiz is vertical
            perpend.h = False
            perpend.v = True
            # get x from point it passes through
            perpend.x = p.x
        else:
            perpend.v = False
            perpend.h = False
            # get negative reciprocal
            perpend.m = self.m.recip(negative=True)
            # find y-intercept of line that passes through point p
            perpend.b = p.y - p.x * perpend.m.get()
        return perpend

    # returns true or false. True if the point is on the line and false otherwise
    def on(self, p:p):
        # if vertical, they just need to share an x-value
        if self.v:
            return self.x == p.x
        # if horizontal, they just need to share a y-value
        elif self.h:
            return self.y == p.y
        else:
            # plug the points x value into the line. If it is the same (or very very close) return true, false otherwise
            return abs(p.y - self.plugin(p.x)) < 0.00000001

    # plugs x into y = mx + b
    def plugin(self, x):
        return self.m.get() * x + self.b

    # Checks to see if two lines intersect. The return value is sort of strange here:
    # returns false if they dont intersect, true if they completely overlap, and returns the point if they intersect at one point
    def intersect(self, line):
        # both vertical, return if they share the same x-intercept
        if self.v and line.v:
            return self.x == line.x
        # both horizontal, return if they share the same y-intercept
        elif self.h and line.h:
            return self.y == line.y
        # one is vertical, see what the y-value is when the other is hitting it
        elif self.v:
            x = self.x
            y = line.plugin(x)
        elif line.v:
            x = line.x
            y = self.plugin(x)
        # one is horizontal, see what the x-value is when the other is hitting it
        elif self.h:
            y = self.y
            x = (y - line.b) / line.m.get()
        elif line.h:
            y = line.y
            x = (y - self.b) / self.m.get()
        # otherwise
        else:
            # check if they share a slope (or very close), if so return whether they share a y-intercept
            if abs(self.m.get() - line.m.get()) < 0.00000001:
                return abs(self.b - line.b) < 0.00000001
            # otherwise set eqations equal, solve for x then plugin for y
            else:
                x = (self.b - line.b) / (line.m.get() - self.m.get())
                y = self.plugin(x)
        return p(x, y)

    # returns whether two points are on the same side of a line. Returns true if either is on the line
    def same_side(self, p1:p, p2:p):
        if self.on(p1) or self.on(p2):
            return True
        elif self.v:
            return (p1.x < self.x) == (p2.x < self.x)
        elif self.h:
            return (p1.y < self.y) == (p2.y < self.y)
        else:
            return (self.plugin(p1.x) > p1.y) == (self.plugin(p2.x) > p2.y)
        
    def __str__(self):
        if self.v:
            return f"vertical line at x={self.x}"
        elif self.h:
            return f"horizontal line at y={self.y}"
        return f"y = {self.m.get()}x + {self.b}"

# class to store a line segment defined by two points.
# subclass of line
class line_segment(line2):

    # stores the minimum and maximum x and y values, essentially creating a rectangle
    # also keeps a value of length
    def __init__(self, p1:p=None, p2:p=None):
        super().__init__(p1, p2)
        if p1 is not None and p2 is not None:
            self.length = p1.distance(p2)
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
        return (p.x >= self.minx and p.x <= self.maxx) and (p.y >= self.miny and p.y <= self.maxy)

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
        if pir.radius.length < pir.treasureline.length:
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
