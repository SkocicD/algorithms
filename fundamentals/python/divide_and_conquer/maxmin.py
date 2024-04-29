import math


def maxmin(a):
    if len(a) == 1:
        return (a[0], a[0])
    u = math.floor(len(a)/2)
    sub1 = maxmin(a[:u])
    sub2 = maxmin(a[u:])
    return (min(sub1[0], sub2[0]), max(sub1[1], sub2[1]))


print(maxmin([1, 2, 3, 4, 1000, -2121, -1, 20, 1, 6, 78, 5, 6, 7, 8]))
