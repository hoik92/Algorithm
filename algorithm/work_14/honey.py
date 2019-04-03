def find_max(tmp, c, x, y):
    global N, M, C, max_tmp
    if tmp > max_tmp:
        max_tmp = tmp
        # cur_max[x][y] = max_tmp
    for i in range(M):
        if c + m[x][y + i] <= C and not catch[i]:
            catch[i] = 1
            find_max(tmp + m[x][y + i] ** 2, c + m[x][y + i], x, y)
            catch[i] = 0


for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    visited = [[0] * N for _ in range(N)]
    # cur_max = [[0] * N for _ in range(N)]
    catch = [0] * M
    result = 0
    # maxx, maxy = 0, 0
    # result1 = 0
    for i in range(N):
        for j in range(N - M + 1):
            max_tmp = 0
            for k in range(M):
                visited[i][j + k] = 1
            find_max(0, 0, i, j)
            tmp_result = max_tmp

            # result2 = cur_max[0][0]
            # for a in range(N):
            #     for b in range(N):
            #         if sum(visited[a][b:b + M]) == 0:
            for a in range(N):
                for b in range(N - M + 1):
                    if sum(visited[a][b:b + M]) == 0:
                        max_tmp = 0
                        find_max(0, 0, a, b)
                        if tmp_result + max_tmp > result:
                            result = tmp_result + max_tmp
            for k in range(M):
                visited[i][j + k] = 0

    print(f"#{tc} {result}")
