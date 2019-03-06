def DFS(x, y, n, k):
    if k == 7:
        if not (n in result):
            result.append(n)
        return
    else:
        for i in range(4):
            if 0 <= x + dx[i] < 4 and 0 <= y + dy[i] < 4:
                DFS(x + dx[i], y + dy[i], n + m[x + dx[i]][y + dy[i]], k + 1)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input())+1):
    m = [0] * 4
    for i in range(4):
        m[i] = input().split()

    result = []
    for i in range(4):
        for j in range(4):
            DFS(i, j, m[i][j], 1)
    print("#{} {}".format(tc, len(result)))