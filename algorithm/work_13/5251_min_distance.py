def find_min(d):
    n = len(d)
    min_dis = 100
    idx = 0
    for i in range(n):
        if d[i] < min_dis and not visited[i]:
            min_dis = d[i]
            idx = i
    return idx


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    m = [[100] * (N + 1) for _ in range(N + 1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        m[s][e] = w
    for i in range(N + 1):
        m[i][i] = 0

    visited = [0] * (N + 1)
    visited[0] = 1
    d = m[0][:]

    while True:
        idx = find_min(d)
        visited[idx] = 1
        if idx == N:
            break

        for i in range(N + 1):
            if m[idx][i] != 100 and not visited[i]:
                if d[i] > d[idx] + m[idx][i]:
                    d[i] = d[idx] + m[idx][i]
    print(f"#{tc} {d[N]}")
