def DFS(n):
    global result, M
    if n == 99:
        result = 1
        return
    for i in range(M):
        if m[i][0] == n and not visited[m[i][1]]:
            visited[m[i][1]] = 1
            DFS(m[i][1])
            visited[m[i][1]] = 0
            if result:
                return

for t in range(1, 11):
    tc, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    m = [0] * M
    for i in range(M):
        m[i] = (tmp[2 * i], tmp[2 * i + 1])

    result = 0
    visited = [0] * 100
    visited[0] = 1
    DFS(0)
    print("#{} {}".format(tc, result))