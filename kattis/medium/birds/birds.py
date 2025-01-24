l, d, n = list(map(int,input().split()))

spaces = [True] * l
if l <= 6:
    print(0)
    exit()

for i in range(6):
    spaces[i] = False
    spaces[-(i+1)] = False


for _ in range(n):
    b = int(input()) - 1
    for i in range(b, b-d, -1):
        if i >= 0 and i < len(spaces):
            if not spaces[i]:
                break
            spaces[i] = False

    for i in range(b+1, b+d):
        print(f'p{i}')
        if i >= 0 and i < len(spaces):
            if not spaces[i]:
                break
            spaces[i] = False


print(spaces)
i = 0
total = 0
while i < len(spaces):
    if spaces[i]:
        total+=1
        i+=d
    i += 1

print(total)
