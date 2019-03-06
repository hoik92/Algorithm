for tc in range(1, int(input())+1):
    s = input()
    N = len(s)
    stack = [0] * N
    stack[0] = s[0]
    top = 0
    count = 0

    for i in range(1, N):
        if top == -1 or stack[top] != s[i]:
            top += 1
            stack[top] = s[i]
        elif stack[top] == s[i]:
            stack[top] = 0
            top -= 1

    for i in stack:
        if i:
            count += 1

    print(f"#{tc} {count}")