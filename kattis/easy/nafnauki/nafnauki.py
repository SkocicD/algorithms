print((s := input())[-s[::-1].index('.')-1:])
