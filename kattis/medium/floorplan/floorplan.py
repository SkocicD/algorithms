#!/usr/bin/python3
n = int(input())
for a in range(1, int(n**.5)+1):
    b = n/a
    if b == int(b):
        m = (a+b)/2
        if b >= m and m == int(m):
            print(int(m), int(b-m))
            exit()
print('impossible')
