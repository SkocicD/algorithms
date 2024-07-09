from functools import cache
a_len = int(input())

arr = [int(x) for x in input().split()]
arr = tuple(arr)


@cache
def calculate_max(a):
    if a == [0, 20, 20, 40]:
        print(a)
    if len(a) == 2:
        return 2
    mx = len(a)
    for i in range(2, len(a)):
        if a[i] != a[i-1] + a[i-2]:
            mx = 2

    for i in range(len(a)):
        tmp = calculate_max(a[0:i] + a[i+1:])
        if mx < tmp:
            mx = tmp

    return mx


print(calculate_max(arr))
