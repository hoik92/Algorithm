for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    min_cnt = 100 * K
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            right, left = 0, 0
            for k in range(K):
                right += m[i + k][j + k]
                left += m[i + k][j + K - 1 - k]
            tmp = abs(right - left)
            if min_cnt > tmp:
                min_cnt = tmp
    print("#{} {}".format(tc, min_cnt))

# 1
# 4 3
# 1 1 2 2
# 4 3 9 3
# 1 4 1 3
# 4 4 4 4