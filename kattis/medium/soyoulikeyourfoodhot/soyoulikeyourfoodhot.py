ps = input().split()
p1, p2, p3 = [int(x.replace('.', '')) for x in ps]
answers = []
for i in range(p1//p2+1):
    temp = p1 - p2 * i
    if temp % p3 == 0:
        other = temp // p3
        answers.append((i, other))
if len(answers) == 0:
    print('none')
[print(*a) for a in answers]
