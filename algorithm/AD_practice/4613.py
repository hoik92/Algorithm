for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = list(input())

    min_cnt = N * M
    for i in range(1, N - 1):
        for j in range(1, N - i):
            w = i
            b = j
            r = N - i - j
            cnt = 0
            for k in range(w):
                for l in range(M):
                    if m[k][l] != 'W':
                        cnt += 1
            for k in range(w, w + b):
                for l in range(M):
                    if m[k][l] != 'B':
                        cnt += 1
            for k in range(w + b, N):
                for l in range(M):
                    if m[k][l] != 'R':
                        cnt += 1
            if min_cnt > cnt:
                min_cnt = cnt
    print("#{} {}".format(tc, min_cnt))