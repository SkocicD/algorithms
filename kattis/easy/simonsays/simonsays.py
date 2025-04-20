for _ in range(int(input())):
    if (s := input())[0:10] == "Simon says":
        print(s[10:])
