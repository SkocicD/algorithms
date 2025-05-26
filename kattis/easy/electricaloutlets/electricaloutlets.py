for _ in range(int(input())):
    print(sum(n := list(map(int, input().split()))[1:])-len(n)+1)
