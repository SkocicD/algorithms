from collections import Counter, OrderedDict
from itertools import pairwise
n=input()
h=list(map(int,input().split()))
h=dict(sorted(dict(Counter(h)).items()))

for a,b in pairwise(h):
    h[b] += h[a]

a,b=(0,len(h)-1)

while a!=b:
    # print("a,b=",a,b)
    i = (a+b)//2
    keys = list(h.keys())
    height = keys[i]
    num_below = h[height]
    # print(i,height,num)
    if height > num_below:
        b = i
    else:
        a = i+1

keys = list(h.keys())
height = keys[a]
num_below = h[height]

if a == 0 and height > num_below:
    print(h[keys[-1]])
elif a == len(keys)-1 and height < num_below:
    print(keys[-1])
else:
    print(a)
    print(keys[a-1])
    print(keys[a-1]+h[keys[-1]]-h[keys[a-1]])
