for tc in range(1, int(input())+1):
    s = input()
    N = len(s)

    stack = [0] * N
    top = -1

    result = 1
    for i in s:
        if i == '(' or i == '{' or i == '[':
            top += 1
            stack[top] = i

        elif i == ')' or i == '}' or i == ']':
            tmp = stack[top]
            top -= 1
            if (i == ')' and tmp != '(') or (i == '}' and tmp != '{') or (i == ']' and tmp != '['):
                result = 0
    if top != -1:
        result = 0

    print(f"#{tc} {result}")