prevch = None
tot = 0
for _ in range(int(input())):
    if prevch == (p := input()):
        tot += 1
    prevch = p
print(tot)
