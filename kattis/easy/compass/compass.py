a,b=(int(input()),int(input()))
if abs(b-a) > 180:
    if b-a<0:
        print(b-a+360)
    elif b-a>0:
        print(b-a-360)
elif abs(b-a) < 180:
    print(b-a)
else:
    print(180)
