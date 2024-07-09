

end_input = '0 0 0.0'
lines = []
inp = input()
while inp != end_input:
    lines.append(inp)
    inp = input()


def check_if_cut(width, points, end):
    highest = 0
    for p in points:
        if highest < p - width / 2:
            return False
        highest = p + width / 2
    return highest >= end


for i in range(0, len(lines), 3):
    width = float(lines[i].split()[2])
    xs = lines[i + 1].split()
    ys = lines[i + 2].split()

    xs = [float(x) for x in xs]
    ys = [float(y) for y in ys]

    xs.sort()
    ys.sort()

    if (check_if_cut(width, xs, 75) and check_if_cut(width, ys, 100)):
        print("YES")
    else:
        print("NO")
