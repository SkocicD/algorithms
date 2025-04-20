m = {}
for _ in range(int(input())):
    input()
    if (s := input()) in m:
        m[s] += 1
    else:
        m[s] = 1
for key in m:
    print(key, m[key])
