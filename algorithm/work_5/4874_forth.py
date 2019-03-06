import sys
sys.stdin = open('input4874.txt', 'r')

def push(s):
    global top
    top += 1
    stack[top] = s

def pop():
    global top
    s = stack[top]
    top -= 1
    return s

for tc in range(1, int(input())+1):
    s = input().split()

    stack = [0] * len(s)
    top = -1
    c = [0] * 2
    result = 0

    for i in s:
        if result:
            break
        if i != '+' and i != '-' and i != '*' and i != '/' and i != '.':
            push(i)
        elif i == '.' and not top:
            result = pop()
        else:
            for j in range(2):
                if top == -1:
                    result = 'error'
                    break
                else:
                    c[j] = int(pop())
            if not result:
                if i == '+':
                    push(c[1] + c[0])
                elif i == '-':
                    push(c[1] - c[0])
                elif i == '*':
                    push(c[1] * c[0])
                elif i == '/' and c[0]:
                    push(c[1] // c[0])
                else:
                    result = 'error'

    print(f"#{tc} {result}")