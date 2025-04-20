ang = max(map(int, (input(), input(), input())))
if ang < 90:
    print("Spetsig Triangel")
elif ang == 90:
    print("Ratvinklig Triangel")
else:
    print("Trubbig Triangel")
