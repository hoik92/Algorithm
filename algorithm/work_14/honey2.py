def find(x, y, tmp, c):
    global N, M, C, result1, maxx, maxy, tmp_result
    if tmp > tmp_result:
        tmp_result = tmp
        cur_max[x][y] = tmp
    for i in range(M):
        if c + m[x][y + i] <= C and not check[i]:
            check[i] = 1
            find(x, y, tmp + m[x][y + i] ** 2, c + m[x][y + i])
            check[i] = 0


for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    visited = [[0] * N for _ in range(N)]
    cur_max = [[0] * (N - M + 1) for _ in range(N)]
    check = [0] * M

    result1 = 0
    maxx, maxy = 0, 0
    for i in range(N):
        for j in range(N - M + 1):
            tmp_result = 0
            find(i, j, 0, 0)
            if tmp_result > result1:
                result1 = tmp_result
                maxx, maxy = i, j

    for i in range(M):
        visited[maxx][maxy + i] = 1

    result2 = 0
    for a in range(N):
        for b in range(N - M + 1):
            if sum(visited[a][b:b + M]) == 0:
                if cur_max[a][b] > result2:
                    result2 = cur_max[a][b]
    print(f"#{tc} {result1 + result2}")

