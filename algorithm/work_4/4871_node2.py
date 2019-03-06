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

    while True:
        while v:
            x = v
            for i in range(1, V+1):
                if m[x][i] and not visited[i]:
                    top += 1
                    stack[top] = x
                    v = i
                    visited[v] += 1
                    break
                else:
                     v = 0
        if top == -1:
            break
        v = stack[top]
        top -= 1

    if visited[G]:
        result = 1

    print(f"#{tc} {result}")
    print(stack)
    print(visited)