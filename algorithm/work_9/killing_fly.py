for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    max_cnt = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            tmp = 0
            for k in range(M):
                for l in range(M):
                    tmp += m[i + k][j + l]
            if tmp > max_cnt:
                max_cnt = tmp
    print("#{} {}".format(tc, max_cnt))