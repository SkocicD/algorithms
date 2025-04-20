a, b = list(map(int, input().split()[::2]))
if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print("Goggi svangur!")
