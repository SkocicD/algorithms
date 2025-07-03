w = input()
out = ''
for i in range(len(c := input()))[::3]:
    out += w[int(c[i:i+3])-1]
print(out)
