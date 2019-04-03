dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    d = [[10000] * N for _ in range(N)]
    d[0][0] = 0
    d[0][1] = m[0][1] + 1
    d[1][0] = m[1][0] + 1

    for _ in range(N):
        for i in range(N):
            for j in range(N):
                for k in range(4):
                    if 0 <= i + dx[k] < N and 0 <= j + dy[k] < N:
                        tmp = m[i + dx[k]][j + dy[k]] - m[i][j]
                        if tmp < 0:
                            tmp = 0
                        tmpx, tmpy = i + dx[k], j + dy[k]
                        if d[tmpx][tmpy] > d[i][j] + tmp + 1:
                            d[tmpx][tmpy] = d[i][j] + tmp + 1
    print(d)
    print(f"#{tc} {d[N - 1][N - 1]}")
