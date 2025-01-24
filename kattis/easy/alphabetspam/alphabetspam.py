w, l, u, o = 0,0,0,0
for c in input():
    if c.isalpha():
        if c.lower() == c:
            l+=1
        else:
            u+=1
    elif c == "_":
        w += 1
    else:
        o +=1
tot = w+l+u+o

print(w/tot)
print(l/tot)
print(u/tot)
print(o/tot)
