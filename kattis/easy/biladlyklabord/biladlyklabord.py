i, j = (0, 0)
s = input()
while i < len(s):
    j = i+1
    while j < len(s) and s[j] == s[i]:
        j += 1
    s = s[:i+1]+s[j:]
    i += 1
print(s)
