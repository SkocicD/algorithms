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

for line in sys.stdin:
    line.replace(' ', '')
    postfix = topostfix(line)
    resolve(postfix)
