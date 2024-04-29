import math


def sort(a):
    if len(a) == 1:
        return (a)
    u = math.floor(len(a)/2)
    sub1 = sort(a[:u])
    sub2 = sort(a[u:])
    return (merge(sub1, sub2))


def merge(a, b):
    ret = []
    while len(a) != 0 and len(b) != 0:
        if (a[0] < b[0]):
            ret.append(a[0])
            a = a[1:]
        else:
            ret.append(b[0])
            b = b[1:]
    if len(b) == 0:
        ret = ret + a
    else:
        ret = ret + b
    return ret


print(sort([1, 2, 3, 4, 1000, -2121, -1, 20, 1, 6, 78, 5, 6, 7, 8]))
