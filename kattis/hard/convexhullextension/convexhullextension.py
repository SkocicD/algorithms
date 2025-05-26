from fractions import Fraction
import math

# Class to store a point object, (x, y)


class p():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class line():
    # create a line object based on two points that it passes through
    # stores the slope and y-intercept, or if it is vertical or horizontal, stores its respective x or y value
    def __init__(self, p1: p, p2: p):
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

    def on(self, p: p):
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
            point = p(Fraction(x, det), Fraction(y, det))
            return point

    def perp(self):
        if self.a == 0:
            return line(p(0, 0), p(0, 1))
        if self.b == 0:
            return line(p(0, 0), p(1, 0))
        slope = Fraction(self.b, self.a)
        return line(p(0, 0), p(1, slope))

    def getx(self, y):
        return (self.c - y * self.b)/self.a

    def gety(self, x):
        return (self.c - x * self.a)/self.b

    def __str__(self):
        return f"{self.a}x + {self.b}y = {self.c}"


class line_segment(line):
    def __init__(self, p1: p, p2: p):
        super().__init__(p1, p2)
        self.p1 = p1
        self.p2 = p2
        self.min_x = min(p1.x, p2.x)
        self.min_y = min(p1.y, p2.y)
        self.max_x = max(p1.x, p2.x)
        self.max_y = max(p1.y, p2.y)

    def in_x_range(self, x):
        return x >= self.min_x and x <= self.max_x

    def in_y_range(self, y):
        return y >= self.min_y and y <= self.max_y

    def length(self):
        return math.sqrt((self.p1.x-self.p2.x)**2 + (self.p1.y-self.p2.y)**2)


class triangle:
    def __init__(self, p1, p2, p3):
        self.ps = [p1, p2, p3]
        self.lines = [line_segment(self.ps[i-1], self.ps[i])
                      for i in range(3)]

        self.minx = min(p1.x, p2.x, p3.x)
        self.miny = min(p1.y, p2.y, p3.y)
        self.maxx = max(p1.x, p2.x, p3.x)
        self.maxy = max(p1.y, p2.y, p3.y)
        self.xrng = self.maxx-self.minx
        self.yrng = self.maxy-self.miny

    def count_added_points(self):

        total = 0
        if self.xrng < self.yrng:
            for x in range(math.floor(self.minx), math.ceil(self.maxx)):
                # the range can go a little above and below.
                if x <= self.minx or x >= self.maxx:
                    continue

                ys = []
                ys = [l.gety(x) for l in self.lines if l.in_x_range(x)]

                bottom = min(ys) + 1
                top = max(ys) - 1

                # subtract highest and lowest point in the current triangle to get the total number of points inside
                if math.ceil(top) >= math.floor(bottom):
                    total += math.ceil(top)-math.floor(bottom) + 1
        else:
            for y in range(math.floor(self.miny), math.ceil(self.maxy)):
                # the range can go a little above and below.
                if y <= self.miny or y >= self.maxy:
                    continue

                xs = [l.getx(y) for l in self.lines if l.in_y_range(y)]

                left = min(xs) + 1
                right = max(xs) - 1

                # subtract rightmnost and leftmost point in the current triangle to get the total number of points inside
                if math.ceil(right) >= math.floor(left):
                    total += math.ceil(right)-math.floor(left) + 1

        return total

    def __str__(self):
        print(f'triangle defined by {self.p1}, {self.p2}, {self.p3}')


n = int(input())
ps = []
lines = []
for _ in range(n):
    ps.append(p(*list(map(int, input().split()))))
for i in range(n):
    lines.append(line_segment(ps[i-1], ps[i]))

total = 0
for i in range(n):

    a = lines[i-2].length()
    b = lines[i-1].length()
    c = line_segment(ps[i-3], ps[i-1]).length()
    A = (a**2+b**2-c**2)/(2*a*b)
    a = b
    b = lines[i].length()
    c = line_segment(ps[i-2], ps[i]).length()
    B = (a**2+b**2-c**2)/(2*a*b)
    angle = math.acos(A*B-math.sqrt((1-A*A)*(1-B*B)))
    print(angle)
    if math.pi < math.2*pi-angle and angle <= 2*math.pi:
        angle = 2*math.pi-angle

    if angle < math.pi:
        print('infinitely many')
        exit()

for i in range(n):
    intersection = lines[i-2].intersect(lines[i])
    if intersection == False:
        perp = lines[i].perp()
        if perp.a == 0 or perp.b == 0:
            dist = line_segment(lines[i].intersect(
                perp), lines[i-2].intersect(perp)).length()
        else:
            dist = line_segment(lines[i].intersect(
                perp), lines[i-2].intersect(perp)).length()
        print(0 if dist <= 1 else 'infinitely many')
        exit()

    tri = triangle(intersection, ps[i-2], ps[i-1])
    total += tri.count_added_points()
    print(total)
