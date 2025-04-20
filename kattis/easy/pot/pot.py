total = 0
for _ in range(int(input())):
    total += int((s := input())[:-1])**int(s[-1])
print(total)
