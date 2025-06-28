n = list(map(int, input().split()))
print((max((n[0]-n[2])**2+(n[1]-n[3])**2, (n[4]-n[6])**2+(n[5]-n[7])**2))**.5)
