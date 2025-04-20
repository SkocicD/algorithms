for _ in range(int(input())):
    k, n = input().split()
    n = int(n)
    ans = [k]
    ans.append(n*(n+1)//2)
    ans.append(ans[-1]*2-n)
    ans.append(ans[-2]*2)
    print(*ans)
