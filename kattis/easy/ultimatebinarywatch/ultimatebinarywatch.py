a, b, c, d = [f'{int(x):04b}'for x in input()]
[print(f'{a[i]} {b[i]}   {c[i]} {d[i]}'.translate({49: 42, 48: 46}))
 for i in range(4)]
