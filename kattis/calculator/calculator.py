import sys

operators = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

def negative_operand(s:str):
    s = s[1:]
    if s[0] == '(':
        s, val = resolve_expression(s[1:])
    else:
        s, val = read_number(s)
    return s, -1 * val

def resolve_expression(s):
    if s[0] == '-':
        s, val = negative_operand(s)
    elif s[0] == '(':
        s = s[1:]
        while s[1] != ')':
            s, val = resolve_expression(s[1:])
        s = 
        s, val = read_number(s)
    
def read_number(s:str):
    i = 0
    while s[i].isdigit():
        i += 1
    num = float(s[0:i])
    s = s[i:]
    return s, num
def topostfix(inp):
    stk = []
    output = []
    num = ''
    prev = ''
    i = 0
    while i < len(inp):
        ch = inp[i]
        if ch.isspace():
            i += 1
            continue

        if (prev in operators or prev == '' or prev == '(') and ch == '-':
            num = float('-1')
            inp = inp[:i + 1] + '*' + inp[i + 1:]
            prev = ch
            # num += '-'
        while ch.isdigit():
            ch = inp[i]
            num += ch
            prev = ch
            i += 1

        else:
            if num != '':
                output.append(float(num))
                num = ''
            if ch == '(':
                stk.append(ch)
            elif ch in operators:
                if len(stk) > 0 and stk[-1] in operators:
                    if operators[stk[-1]] < operators[ch]:
                        stk.append(ch)
                    else:
                        output.append(stk.pop())
                        stk.append(ch)
                else:
                    stk.append(ch)
            elif ch == ')':
                while stk[-1] != '(':
                    output.append(stk.pop())
                stk.pop()
            prev = ch
        i += 1
    if num != '':
        output.append(float(num))
    while len(stk) > 0:
        output.append(stk.pop())
    return output

def resolve(postfix):
    print(postfix)
    stk = []
    for item in reversed(postfix):
        stk.append(item)
        while len(stk) > 2 and isinstance(stk[-2], float) and isinstance(stk[-1], float):
            v1 = stk.pop()
            v2 = stk.pop()
            op = stk.pop()
            match(op):
                case '+':
                    stk.append(v1 + v2)
                case '-':
                    stk.append(v1 - v2)
                case '*':
                    stk.append(v1 * v2)
                case '/':
                    stk.append(v1 / v2)

    print(f"{stk.pop():0.2f}")


for line in sys.stdin:
    postfix = topostfix(line)
    resolve(postfix)
