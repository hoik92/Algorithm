def process(x, y, drt, stone, target):
    global N

    if 0 <= x + dx[drt] < N and 0 <= y + dy[drt] < N:
        if m[x + dx[drt]][y + dy[drt]] == target:
            result = process(x + dx[drt], y + dy[drt], drt, stone, target)
            if result:
                m[x][y] = stone
                return 1
            else:
                return 0
        elif m[x + dx[drt]][y + dy[drt]] == stone:
            m[x][y] = stone
            return 1
        else:
            return 0
    else:
        return 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = [[0] * N for _ in range(N)]
    n = N // 2
    m[n][n - 1], m[n - 1][n], m[n][n], m[n - 1][n - 1] = 1, 1, 2, 2

    for i in range(M):
        row, col, stone = list(map(int, input().split()))
        row -= 1
        col -= 1
        m[col][row] = stone
        if stone == 1:
            target = 2
        else:
            target = 1
        for j in range(8):
            if 0 <= col + dx[j] < N and 0 <= row + dy[j] < N:
                if m[col + dx[j]][row + dy[j]] == target:
                    process(col + dx[j], row + dy[j], j, stone, target)
    white, black = 0, 0
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                black += 1
            elif m[i][j] == 2:
                white += 1
    print("#{} {} {}".format(tc, black, white))