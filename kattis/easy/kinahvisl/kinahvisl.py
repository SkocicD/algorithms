c = 1
for a, b in zip(input(), input()):
    c += 1 if a != b else 0
print(c)
