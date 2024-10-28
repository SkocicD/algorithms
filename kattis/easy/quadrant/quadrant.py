x = input()
y = input()
if '-' in x:
    if '-' in y:
        print(3)
    else:
        print(2)
else:
    if '-' in y:
        print(4)
    else:
        print(1)
