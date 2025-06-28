s = input()
a = [ord(c) - 65 for c in s[:len(s)//2]]
b = [ord(c) - 65 for c in s[len(s)//2:]]
rot = sum(a)
a = [(n + rot) % 26 for n in a]
rot = sum(b)
b = [(n + rot) % 26 for n in b]
a = [chr((n + m) % 26 + 65) for n, m in zip(a, b)]
print(''.join(a))
