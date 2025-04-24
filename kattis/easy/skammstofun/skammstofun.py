input()
s = ''
for w in input().split():
    s += (w[0] if w[0] < 'a' else '')
print(s)
