for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if m[i][j]:
                tmp += 1
            else:
                if tmp == K:
                    cnt += 1
                tmp = 0
            if j == N - 1 and tmp == K:
                cnt += 1
    for i in range(N):
        tmp = 0
        for j in range(N):
            if m[j][i]:
                tmp += 1
            else:
                if tmp == K:
                    cnt += 1
                tmp = 0
            if j == N - 1 and tmp == K:
                cnt += 1
    print("#{} {}".format(tc, cnt))