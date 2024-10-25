n1 = input()
n2 = input()

if len(n1) > len(n2):
    n2 = '0' * (len(n1)-len(n2)) + n2
else:
    n1 = '0' * (len(n2)-len(n1)) + n1

m1 = ''
m2 = ''

for i in range(len(n1)):
    if n1[i] > n2[i]:
        m1 += n1[i]
    elif n1[i] == n2[i]:
        m1 += n1[i]
        m2 += n2[i]
    else:
        m2 += n2[i]

if len(m1) == 0:
    print('YODA')
else:
    print(int(m1))


if len(m2) == 0:
    print('YODA')
else:
    print(int(m2))
