import sys
sys.stdin = open('input1.txt', 'r')

def prior(s):
    if s == '*':
        return 5
    elif s == '+':
        return 4
    elif s == '(':
        return 3
    elif s == ')':
        return 2
    else:
        return 1

def push(s):
    global top
    top += 1
    stack[top] = s

def pop():
    global top
    s = stack[top]
    top -= 1
    return s

for tc in range(1, 11):
    N = int(input())
    s = input()

    stack = [0] * N
    top = -1

    result = [-1] * N
    idx = 0

    c = [0] * 2

    for i in s:
        if prior(i) == 1:
            result[idx] = int(i)
            idx += 1
        elif prior(i) == 3:
            push(i)
        elif prior(i) == 2:
            while stack[top] != '(':
                result[idx] = pop()
                idx += 1
            top -= 1
        elif prior(i) > prior(stack[top]):
            push(i)
        else:
            while top != -1 and prior(i) <= prior(stack[top]):
                result[idx] = pop()
                idx += 1
            push(i)
    while top != -1:
        result[idx] = pop()
        idx += 1

    for i in result:
        if i == -1:
            break
        if i != '*' and i != '+':
            push(i)
        else:
            c[0] = pop()
            c[1] = pop()
            if i == '*':
                push(c[1] * c[0])
            else:
                push(c[1] + c[0])

    print(f"#{tc} {stack[top]}")