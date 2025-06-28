st = input().split(';')
total = 0
for s in st:
    if '-' in s:
        n1, n2 = list(map(int, s.split('-')))
        total += n2-n1 + 1
    else:
        total += 1
print(total)
