w, a = (input(), input())
total, n = (0, len(w))
for i in range(len(s := input())-n+1):
    if s[i:i+n] == w:
        total += 1
print(total)
