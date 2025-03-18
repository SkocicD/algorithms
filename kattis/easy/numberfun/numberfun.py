for n in range(int(input())):
    a,b,c=list(map(int,input().split()))
    print("Possible" if a+b==c or abs(a-b)==c or a*b==c or a/b==c or b/a==c else "Impossible")
