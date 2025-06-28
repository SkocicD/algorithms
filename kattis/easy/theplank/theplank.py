n = int(input())
l = [1, 1, 2]
while len(l) < n+1:
    l.append(sum(l[-3:]))
    # print(l)
print(l[-1])
