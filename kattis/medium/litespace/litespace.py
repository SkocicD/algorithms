s = input()
stk = []

def nextchar():
    global char
    global s
    char = s[0]
    s=s[1:]

def read_integer():
    global char
    nextchar()
    sign = -1 if char == "T" else 1
    nextchar()
    num = 0
    while char != 'N':
        num = num << 1

        if char == 'T':
            num += 1

        nextchar()
    return num * sign

def next_instruction():
    global char
    word = ''
    while word not in {'SS','SNS','SNT','SNN','TSSS','TSST','TSSN','TSTS','TNST'}:
        nextchar()
        word += char

    match word:
        case 'SS':
            stk.append(read_integer())
        case 'SNS':
            if len(stk) == 0:
                print('Invalid copy operation')
            else:
                stk.append(stk[-1])
        case 'SNT':
            if len(stk) < 2:
                print('Invalid swap operation')
            else:
                a = stk.pop()
                b = stk.pop()
                stk.append(a)
                stk.append(b)
        case 'SNN':
            if len(stk) == 0:
                print('Invalid remove operation')
            else:
                stk.pop()
        case 'TSSS':
            if len(stk) < 2:
                print('Invalid addition operation')
            else:
                a = stk.pop()
                b = stk.pop()
                stk.append(a+b)
        case 'TSST':
            if len(stk) < 2:
                print('Invalid subtraction operation')
            else:
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
        case 'TSSN':
            if len(stk) < 2:
                print('Invalid multiplication operation')
            else:
                a = stk.pop()
                b = stk.pop()
                stk.append(b*a)
        case 'TSTS':
            if len(stk) < 2:
                print('Invalid division operation')
            else:
                a = stk.pop()
                b = stk.pop()
                if a == 0:
                    print('Division by zero')
                    stk.append(b)
                    stk.append(a)
                else:
                    stk.append(int(b/a))
        case 'TNST':
            if len(stk) < 1:
                print('Invalid print operation')
            else:
                print(stk.pop())

while len(s) > 0:
    next_instruction()


