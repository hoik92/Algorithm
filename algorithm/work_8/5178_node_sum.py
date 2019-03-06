for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    value = [0] * (2 * N)
    for i in range(M):
        idx, x = map(int, input().split())
        value[idx] = x

    for i in range(N, 0, -1):
        if value[i] == 0:
            value[i] = value[2 * i] + value[2 * i + 1]

    print("#{} {}".format(tc, value[L]))