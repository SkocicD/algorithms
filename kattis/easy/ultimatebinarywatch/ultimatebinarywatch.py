n=[f'{int(x):04b}' for x in input()]
[print(f'{n[0][i]} {n[1][i]}   {n[2][i]} {n[3][i]}'.replace('0','.').replace('1','*')) for i in range(4)]
