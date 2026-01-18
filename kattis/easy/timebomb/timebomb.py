m = [245, 80, 103, 87, 210, 151, 183, 84, 247, 215]
s = [0]*10
for j in range(10):
    n = m[j]
    i = 0
    while n:
        b = n & 1
        s[j] |= 7*b << (6*i) if i < 4 else 73*b << 2*(i % 2)+6*(i > 5)
        n >>= 1
        i += 1

a = 0
for r in open(0):
    k = int(len(r)/4)
    if not a:
        a = ['']*k
    for i in range(0, k):
        a[i] += r[i*4:i*4+3]
for i in range(len(a)):
    a[i] = int(a[i].replace("*", "1").replace(" ", "0"), 2)

num = 0
for i in range(1, len(a)+1):
    if a[-i] not in s:
        num = 1
        break
    else:
        num += s.index(a[-i])*(10**(i-1))
print('BEER!!' if num % 6 == 0 else 'BOOM!!')
