import math

w, p = input().split()
w = int(w)
p = int(p)

x, y = input().split()
treasure = p(int(x), int(y))

walls = []
pirates = []

for _ in range(w):
    x1, y1, x2, y2 = [int(z) for z in input().split()]
    walls.append((p(x1, y1), p(x2, y2)))

for _ in range(p):
    x1, y1, x2, y2 = [int(z) for z in input().split()]
    pirates.append((p(x1, y1), p(x2, y2)))

print(walls)
print(pirates)


class p():
    def __init__(x, y):
        self.x = x
        self.y = y

    def distance(p2):
        return math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2)


class fraction():
    def __init__(num, denom):
        self.n = num
        self.d = denom

    def get():
        return self.n / self.d

    def recip(negative=False):
        if negative:
            return fraction(-self.d, self.n)
        else:
            return fraction(self.d, self.n)


class line():
    def __init__(self, p1=None, p2=None):
        if p1 is not None and p2 is not None:
            if p1.x == p2.x:
                self.v = True
                self.h = False
                self.x = p1.x
            elif p1.y == p2.y:
                self.v = False
                self.h = True
                self.y = p1.y
            else:
                self.v = False
                self.h = False
                self.m = fraction(p1.y-p2.y, p1.x-p2.x)
                self.b = p1.y - p1.x * self.m.get()

    def perp(self, p):

        perpend = line()
        if self.v:
            perpend.h = True
            perpend.v = False
            perpend.y = p.y
        elif self.h:
            perpend.h = False
            perpend.v = True
            perpend.x = p.x
        else:
            perpend.v = False
            perpend.h = False
            perpend.m = self.m.recip(negative=True)
            self.b = p.y - p.x * perpend.m.get()
        return perpend

    def on(self, p):
        if self.v:
            return self.x == p.x
        elif self.h:
            return self.y == p.y
        else:
            return p.y == self.plugin(p.x)

    def plugin(self, x):
        return self.m.get() * x + self.b

    def intersect(self, lne):
        if self.v and lne.v:
            return self.x == lne.x
        elif self.h == self.h:
            return self.y == lne.y
        elif self.v:
            x = self.x
            y = lne.plugin(self.x)
        elif lne.v:
            x = lne.x
            y = self.plugin(x)
        elif self.h:
            x = (self.y - lne.b) / lne.m.get()
            y = self.y
        elif lne.h:
            x = (lne.y - self.b) / self.m.get()
            y = lne.y
        else:
            x = (self.b - lne.b) / (lne.m - self.m)
            y = self.plugin(x)
        return p(x, y)

    def same_side(self, p1, p2):
        if self.on(p1) or self.on(p2):
            return True
        elif self.v:
            return (p1.x < self.x) == (p2.x < self.x)
        elif self.h:
            return (p1.y < self.y) == (p2.y == self.y)
        else:
            return (self.plugin(p1.x) > p1.y) == (self.plugin(p2.x) > p2.y)


if __name__ == '__main__':
    kept_pirates = []
    current_pirates = [p for p in pirates]
    # start by checking which points are within range of
    for curpir in current_pirates:
        p1, p2 = curpir
        if p1.distance(p2) >= p1.distance(treasure):
            kept_pirates.append(curpir)

    print(kept_pirates)

    # next remove pirates that are not looking in the right direction
    current_pirates = [p for p in kept_pirates]
    kept_pirates = []

    for curpir in current_pirates:
        p1, p2 = curpir
        curline = line(p1, p2)
        perpline = curline.perp(p1)
        if perpline.same_side(p2, treasure):
            kept_pirates.append(curpir)

    # remove pirates that are have a wall blocking them
    current_pirates = [p for p in kept_pirates]
    kept_pirates = []

    for curpir in current_pirates:
        p1, p2 = curpir
        curline = line(p1, treasure)
        for wall in walls:
            w1, w2 = wall
            curwall = line(w1, w2)
            intersection = curline.intersect(curwall)
            if intersection == False:
                continue
            else:
                if cur
    for cp in current_pirates:
        p1, p2 = cp
        eq = eqn(p1, p2)
        for p in pirates:
            if cp != p and on(eq, p[0]):
                break
        else:
            kept_pirates.append(cp)

    current_pirates = [p for p in kept_pirates]
    kept_pirates = []

    for

    print(kept_pirates)
