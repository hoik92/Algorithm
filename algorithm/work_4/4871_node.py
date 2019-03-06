for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    m = [0] * (V+1)
    for i in range(V+1):
        m[i] = [0] * (V+1)

    for i in range(E):
        S, G = map(int, input().split())
        m[S][G] += 1

    S, G = map(int, input().split())
    stack = [0] * V
    visited = [0] * (V+1)
    top = -1
    result = 0

    v = S
    visited[v] += 1

    while not result:
        for i in range(1, V+1):
            if m[v][i] and not visited[i]:
                top += 1
                stack[top] = v
                w = i
                break
            else:
                w = 0

        if top == -1:
            break

        while w:
            if w == G:
                result = 1
                break

            visited[w] += 1
            top += 1
            stack[top] = w
            v = w
            for i in range(1, V+1):
                if m[v][i] and not visited[i]:
                    w = i
                    break
                else:
                    w = 0
        v = stack[top]
        top -= 1

    print(f"#{tc} {result}")