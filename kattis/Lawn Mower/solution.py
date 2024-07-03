

end_input = '0 0 0.0'

inp = input()
while inp != end_input:
    width = float(inp.split()[2])
    xs = input().split()
    ys = input().split()
    inp = input()

    xs = [float(x) for x in xs]
    ys = [float(y) for y in ys]

    xs.sort()
    ys.sort()

    highest = 0
    print()
    print(xs)
    print(ys)
    for x in xs:
        print(f"--{highest}**{x}")
        if x - width/2 > highest:
            break
        else:
            highest = x + width/2
    else:
        if highest >= 75:
            print("YES")
            continue
    print(f"   highest     {highest}")
    highest = 0
    for y in ys:
        if y - width/2 > highest:
            break
        else:
            highest = y + width/2
    else:
        if highest >= 100:
            print("YES")
            continue
    print(f"   highest     {highest}")
    print("NO")
