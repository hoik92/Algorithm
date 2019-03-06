for tc in range(1, 11):
    V, E = map(int, input().split())
    m = [0] * (V+1)
    for i in range(V+1):
        m[i] = [0] * (V+1)
    input_degree = [0] * (V + 1)

    stack = [0] * V
    top = -1

    E_list = list(map(int, input().split()))
    for i in range(E):
        x, y = E_list[2 * i], E_list[2 * i + 1]
        m[x][y] = 1

    for i in range(1, V+1):
        for j in range(1, V+1):
            if m[i][j]:
                input_degree[j] += 1

    for _ in range(V):
        for j in range(1, V+1):
            if not input_degree[j] and not j in stack:
                x = j
                top += 1
                stack[top] = x
                break
        for j in range(1, V+1):
            if m[x][j]:
                m[x][j] -= 1
                input_degree[j] -= 1

    print(f"#{tc} ", end='')
    for i in stack:
        print(i, end=' ')
    print()