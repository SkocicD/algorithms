x = int(input())*((n := int(input()))+1)
print(x-sum(int(input()) for _ in range(n)))
