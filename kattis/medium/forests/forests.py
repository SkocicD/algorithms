p, t = input().split()
mp = {}

for i in range(int(p)):
    mp[i+1] = set()

try:
    inp = input()
except EOFError:
    inp = ''

while inp != '':
    p, t = inp.split()
    mp[int(p)].add(int(t))
    try:
        inp = input()
    except EOFError:
        inp = ''

opinions = []

for m in mp:
    if mp[m] not in opinions:
        opinions.append(mp[m])

print(len(opinions))
