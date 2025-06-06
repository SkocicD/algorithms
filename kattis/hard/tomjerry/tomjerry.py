import time
from math import comb
from functools import cache

starttime = time.perf_counter()


def isInside(cheese1, cheese2):
    return cheese1[0] <= cheese2[0] and cheese1[1] <= cheese2[1] and cheese1 != cheese2


X, Y = list(map(int, input().split()))

cheeses = []
numcheeses = int(input())
if numcheeses == 0:
    print(0)
    exit()
for i in range(numcheeses):
    cheeses.append(tuple(map(int, input().split())))
cheeses = sorted(cheeses, key=lambda t: (t[0], t[1]), reverse=True)
for i in range(numcheeses):
    cheeses[i] = (i, cheeses[i])
# print(cheeses)

start = (i+1, (1, 1))
end = (i+2, (X, Y))
tree = {}


def addtotree(currtree, cheese):
    currtree[cheese] = {}
    for treecheese in currtree:
        if isInside(cheese[1], treecheese[1]):
            addtotree(currtree[treecheese], cheese)


for cheese in cheeses:
    addtotree(tree, cheese)
# print(tree)

cheeses.append(start)
cheeses.append(end)


@cache
def paths_between(inner, outer):
    if inner[0] > outer[0] or inner[1] > outer[1]:
        return 0
    n = outer[0]-inner[0]+outer[1]-inner[1]
    k = min(outer[0]-inner[0], outer[1]-inner[1])
    return comb(n, k) % 1000000007


pathfindingtimestart = time.perf_counter()
# calculate paths between table
paths = [[0 for i in range(numcheeses+2)] for j in range(numcheeses+2)]
for cheese1 in cheeses:
    for cheese2 in cheeses:
        i = cheese1[0]
        j = cheese2[0]
        paths[i][j] = paths_between(cheese1[1], cheese2[1])

pathfindingtimeend = time.perf_counter()
print(time.perf_counter() - pathfindingtimestart)

# [print(row) for row in paths]

total = 0

# print(tree)


def traverse(tree, depth=0, product=1, parent=end):
    global total
    if tree == {}:
        return

    for cheese in tree:
        # print(cheese, parent)
        currproduct = product
        currproduct *= paths[cheese[0]][parent[0]]
        # print(currproduct)
        traverse(tree[cheese], depth + 1, currproduct, cheese)
        therest = currproduct*paths[start[0]][cheese[0]]
        # print(therest)
        if depth % 2 == 0:
            total += therest
        else:
            total -= therest


traverse(tree)

print(total % 1000000007)

print(time.perf_counter() - starttime)
# #     for cheese in cheeses:
# #     xcheese, ycheese = cheese
# #     n1 = xcheese + ycheese - 2
# #     k1 = min(xcheese, ycheese)-1
# # print(total % 1000000007)
