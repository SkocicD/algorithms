
k = int(input())
s1 = input()
s2 = input()

match, diff, mx = (0,0,0)

for a, b in zip(s1,s2):
    if a == b:
        match += 1
    else:
        diff += 1


if match <= k:
    mx = 2 * match + diff -k
else:
    mx = k + diff

print(mx)
