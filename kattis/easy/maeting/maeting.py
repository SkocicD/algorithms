input()
a = input().split()
b = set(input().split())
s = ''
for x in a:
    if x in b:
        s += x+' '

print(s[:-1])
