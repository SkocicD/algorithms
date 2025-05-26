inp = input()
out = inp[0]
for c in inp[1:]:
    if c != out[-1]:
        out = out + c
print(out)
