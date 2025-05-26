d, m = list(map(int, input().split()))
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(days[(sum(monthdays[:m-1])+d+2) % 7])
