import sys
lines = []
for line in sys.stdin:
    lines.append(line.strip())
for line1, line2 in zip(lines[::2], lines[1::2]):
    bottom = list(map(float, line1.split()))
    top = list(map(float, line2.split()))
    difference = [t-b for b, t in zip(bottom, top)]
    c, b, a = [difference[1], 2*difference[2], 3*difference[3]]
    possiblex = [1, 0]
    if (disc := b**2-4*a*c) >= 0:
        xlow = (-b-disc**.5)/(2*a)
        xhigh = (-b+disc**.5)/(2*a)
        if 0 < xlow and xlow < 1:
            possiblex.append(xlow)
        if 0 < xhigh and xhigh < 1:
            possiblex.append(xhigh)
    difference[0] -= min([difference[0]+difference[1]*x+difference[2]
                          * x**2+difference[3]*x**3 for x in possiblex])
    print(max([difference[0]+difference[1]*x+difference[2]
               * x**2+difference[3]*x**3 for x in possiblex]))
