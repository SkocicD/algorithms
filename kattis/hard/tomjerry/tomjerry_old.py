from math import comb
from functools import cache


def isInside(cheese1, cheese2):
    return cheese1[0] <= cheese2[0] and cheese1[1] <= cheese2[1] and cheese1 != cheese2


X, Y = list(map(int, input().split()))

cheeses = []
numcheeses = int(input())
for i in range(numcheeses):
    cheeses.append(tuple(map(int, input().split())))
cheeses = sorted(cheeses, key=lambda t: (t[0], t[1]), reverse=True)

end = (X, Y)
tree = {}


def addtotree(currtree, cheese):
    currtree[cheese] = {}
    for treecheese in currtree:
        if isInside(cheese, treecheese):
            addtotree(currtree[treecheese], cheese)


for cheese in cheeses:
    addtotree(tree, cheese)
# print(tree)


@cache
def paths_between(inner, outer):
    n = outer[0]-inner[0]+outer[1]-inner[1]
    k = min(outer[0]-inner[0], outer[1]-inner[1])
    return comb(n, k) % 1000000007


# calculate paths between table
# paths = [[0 for i in range(numcheeses+2)] for j in range(numcheeses+2)]
# print(paths)
# positions
# for i in range(numcheeses+2):
#     for j in range(numcheeses+2):
#         paths[i][j] =


total = 0


def traverse(tree, depth=0, product=1, parent=end):
    global total
    if tree == {}:
        return
    for cheese in tree:
        currproduct = product
        currproduct *= paths_between(cheese, parent)
        traverse(tree[cheese], depth + 1, currproduct, cheese)
        therest = currproduct*paths_between((1, 1), cheese)
        if depth % 2 == 0:
            total += therest
        else:
            total -= therest


traverse(tree)

print(total % 1000000007)

# #     for cheese in cheeses:
# #     xcheese, ycheese = cheese
# #     n1 = xcheese + ycheese - 2
# #     k1 = min(xcheese, ycheese)-1
# # print(total % 1000000007)
