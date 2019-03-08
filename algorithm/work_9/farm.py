for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(input())

    value = 0
    for i in range(N // 2 + 1):
        value += int(m[i][N // 2])
        for j in range(1, i + 1):
            value += int(m[i][N // 2 + j]) + int(m[i][N // 2 - j])
    for i in range(N // 2):
        value += int(m[N - 1 - i][N // 2])
        for j in range(1, i + 1):
            value += int(m[N - 1 - i][N // 2 + j]) + int(m[N - 1 - i][N // 2 - j])
    print("#{} {}".format(tc, value))