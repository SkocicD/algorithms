lst = []
for _ in range(int(input())):
    lst.append(int(input()))

print(0 if (n := min(lst)-max(lst)/2) < 0 else int(n))
