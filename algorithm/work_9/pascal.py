for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = [1] * (i + 1)
        n = len(m[i])
        if n > 2:
            for j in range(1, n - 1):
                m[i][j] = m[i - 1][j - 1] + m[i - 1][j]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()