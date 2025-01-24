num_lines = int(input())

sum = 0
values = []

for i in range(num_lines):
    s, f = input().split()
    values.append(float(f))

values.sort(reverse=True)

for i, f in enumerate(values):
    sum += (i + 1) * f

print(sum)
