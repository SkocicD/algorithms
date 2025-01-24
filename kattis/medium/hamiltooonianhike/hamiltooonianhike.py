import sys

class cabin:
    def __init__(self, num):
        self.num = num
        self.adj = []
        self.visited = False

    def add(self, cabin):
        self.adj.append(cabin)

    def __hash__(self):
        return hash(self.num)

    def __eq__(self, other):
        return self.num == other.num


input = sys.stdin.readlines()
cabins = {}

for line in input:
    a, b = list(map(int, line.split()))
    c1 = cabin(a)
    c2 = cabin(b)
    if a not in cabins:
        cabins[a] = cabin(a)
    if not b in cabins:
        cabins[b] = cabin(b)
    c1 = cabins[a]
    c2 = cabins[b]

    c2.add(c1)
    c1.add(c2)

print(c1.adj)
