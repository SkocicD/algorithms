input()
print(sum(1 if n < 0 else 0 for n in map(int, input().split())))
