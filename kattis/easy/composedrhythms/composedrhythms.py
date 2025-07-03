n = int(input())
l = [2]*(n//2)
if n % 2 == 1:
    l[-1] += 1
print(len(l))
print(*l)
