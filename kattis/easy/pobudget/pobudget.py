total = 0
for _ in range(int(input())):
    input()
    total += int(input())
if total < 0:
    print("Nekad")
elif total > 0:
    print("Usch, vinst")
else:
    print("Lagom")
