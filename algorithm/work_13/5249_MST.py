def find_min(d):
    global V
    min_val = 100
    idx = 0
    for i in range(V + 1):
        if d[i] < min_val and not visited[i]:
            min_val = d[i]
            idx = i
    return idx


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    m = [[100] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        m[n1][n2] = w
        m[n2][n1] = w
    for i in range(V + 1):
        m[i][i] = 0

    visited = [0] * (V + 1)
    visited[0] = 1
    d = m[0][:]
    while True:
        idx = find_min(d)
        visited[idx] = 1
        if sum(visited) == V + 1:
            break

        for i in range(V + 1):
            if m[idx][i] != 100 and not visited[i]:
                if d[i] > m[idx][i]:
                    d[i] = m[idx][i]
    print(f"#{tc} {sum(d)}")
