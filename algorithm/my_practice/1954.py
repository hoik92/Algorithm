def ekfvoddl(x, y, drt, val):
    global N
    if val == N * N:
        return
    if not (0 <= x + dx[drt] < N and 0 <= y + dy[drt] < N and not visited[x + dx[drt]][y + dy[drt]]):
        drt = (drt + 1) % 4
    visited[x + dx[drt]][y + dy[drt]] = 1
    m[x + dx[drt]][y + dy[drt]] = val + 1
    ekfvoddl(x + dx[drt], y + dy[drt], drt, val + 1)


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input())+1):
    N = int(input())
    m = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    drt = 0
    m[0][0] = 1
    visited[0][0] = 1
    ekfvoddl(0, 0, drt, 1)
    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(m[i][j], end=' ')
        print()
