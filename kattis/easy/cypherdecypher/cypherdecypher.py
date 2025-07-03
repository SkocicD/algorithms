dig = [int(c) for c in input()]
for _ in range(int(input())):
    s = ''
    for i, ch in zip(dig, input()):
        s += chr(65+((ord(ch)-65)*i) % 26)
    print(s)
