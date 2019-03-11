for tc in range(1, int(input())+1):
    M, K = map(int, input().split())
    result = [[0, 1, 2, 3, 4, 5, 6]]
    a = []
    b = []
    for i in range(M):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    tmp = [0, 1, 2, 3, 4, 5, 6]
    cnt = 0
    idx = 0

    while True:
        tmp[a[idx] - 1], tmp[b[idx] - 1] = tmp[b[idx] - 1], tmp[a[idx] - 1]
        cnt += 1
        if tmp != result[0] or idx != M - 1:
            result.append(tmp[:])
        else:
            break
        idx = (idx + 1) % M
    k = K % cnt
    print("#{}".format(tc), end=' ')
    for i in range(7):
        print(result[k][i], end='')
    print()