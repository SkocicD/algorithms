total = 0
prev = None
for _ in range(int(input())):
    curr = input()
    if curr == 'sober' and prev == 'drunk':
        total += 1
    prev = curr
print(total)
