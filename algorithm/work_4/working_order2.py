for tc in range(1, 11):
    V, E = map(int, input().split())
    m = [0] * (V+1)
    for i in range(V+1):
        m[i] = [0] * (V+1)
    input_degree = [0] * (V + 1)

    visited = [0] * (V+1)
    stack = [0] * V
    top = -1

    E_list = list(map(int, input().split()))
    for i in range(E):
        x, y = E_list[2 * i], E_list[2 * i + 1]
        m[y][x] = 1

    for i in range(1, V+1):
        for j in range(1, V+1):
            if m[i][j]:
                input_degree[j] += 1


    print(f"#{tc}", end=' ')
    tmp, v = 1, 1
    while True:
        for i in range(tmp, V+1):
            if not input_degree[i]:
                v = i
                tmp = i + 1
                break
            else:
                v = 0

        if not v:
            break

        visited[v] = 1
        result = v
        while True:
            while v:
                x = v
                for i in range(1, V+1):
                    if m[x][i] and not visited[i]:
                        visited[i] = 1
                        top += 1
                        stack[top] = x
                        v = i
                        break
                    else:
                        v = 0

            if top == -1:
                break

            print(x, end=' ')
            v = stack[top]
            top -= 1
        print(result, end=' ')
    print()