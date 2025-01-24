s = input()

d = {'T':0,
     'C':0,
     'G':0
     }

for i in range(len(s)):
    c = s[i]
    if c not in d:
        d[c] = 0
    d[c] += 1
# print(d)

min = 99999999
total = 0
for key in d:
    if d[key] < min:
        min = d[key]
    total += d[key] ** 2

total+=7*min
print(total)
