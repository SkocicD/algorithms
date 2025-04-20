from math import prod
w = int(input())
print(sum(prod(map(int, input().split())) for x in range(int(input())))//w)
