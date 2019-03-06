for tc in range(1, 11):
    N = int(input())
    m = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N - 2):
        if m[i] > m[i - 1] and m[i] > m[i - 2] and m[i] > m[i + 1] and m[i] > m[i + 2]:
            cnt += m[i] - max([m[i - 1], m[i - 2], m[i + 1], m[i + 2]])
    print("#{} {}".format(tc, cnt))