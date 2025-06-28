n = int(input())
print(sum([x for x in range(n+1)]))
print(sum([sum([x for x in range(i+1)]) for i in range(1, n+1)]))
