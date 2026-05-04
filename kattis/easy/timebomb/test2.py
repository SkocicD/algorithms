b=[int(str(x)[1:46:3],2)for x in zip(*(iter(i//42for i in sum(zip(*open(x:=0,'rb')),())),)*20)]
[x:=10*x+'縿庽嚿炟皷纷䈟线皿'.find(chr(y))for y in b]
print('BOOM!!'if x%6else'BEER!!')
