m = {}
for _ in range(int(input())):
    n = input()
    m[n] = [input(), 0]

for _ in range(int(input())):
    try:
        m[input()][1] += 1
    except KeyError:
        pass


h = max(m.values(), key=lambda x: x[1])
for k in m:
    if m[k][1] == h[1] and m[k][0] != h[0]:
        print('tie')
        exit()
print(h[0])

# print("tie" if sum(1 for x in m if (lambda y: y[1] == h[1])(x)) > 1 else h[0])
