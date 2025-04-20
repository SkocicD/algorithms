input()
a = [int(x) for x in input().split() if x != '-1']
print(sum(a)/len(a))
