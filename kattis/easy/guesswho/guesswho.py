N, M, Q = list(map(int, input().split()))
characters = []
for i in range(1, N+1):
    characters.append((i, input()))
for _ in range(Q):
    i, A = input().split()
    characters = [
        character for character in characters if character[1][int(i)-1] == A]
if len(characters) == 1:
    print(f'unique\n{characters[0][0]}')
else:
    print(f'ambiguous\n{len(characters)}')
