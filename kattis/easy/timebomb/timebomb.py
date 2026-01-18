m=''.join
c=[32319,31,24253,22207,28831,30391,32439,16927,32447,30399]
b=[*map(m,zip(*open(x:=0)))]
while b:
 if(d:=int(m('01'[c>' ']for c in m(b[:3])),2))not in c:x=1;break
 x=x*10+c.index(d)
 b=b[4:]
print('BOOM!!'if x%6else'BEER!!')
