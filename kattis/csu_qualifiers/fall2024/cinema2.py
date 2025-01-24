n, m = [int(x) for x in input().split()]

gs = [int(x) for x in input().split()]
total = 0
count = 0
for g in gs:
    total += g
    if total <= n:
        count+=1
    else:
        break

print(m-count)



