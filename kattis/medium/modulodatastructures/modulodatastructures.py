N, Q = list(map(int, input().split()))
array = [0 for x in range(N+1)]

operations = []
followingprints = 0
for _ in range(Q):
    line = list(map(int, input().split()))
    operations.append(line)
    if line[0] == 2:
        followingprints += 1
cached = []
for op in operations:
    print(followingprints)
    if op[0] == 1:
        a, b, c = op[1:]
        if followingprints > (N+1)//b:
            for i in range(a, N+1, b):
                array[i] += c
        else:
            cached.append((a, b, c))
    else:
        followingprints -= 1
        print(array[op[1]]+sum([c for a, b, c in cached if op[1] % b == a]))
