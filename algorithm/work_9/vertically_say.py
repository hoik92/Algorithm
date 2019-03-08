for tc in range(1, int(input())+1):
    m = [0] * 5
    n = 0
    for i in range(5):
        m[i] = input()
        tmp = len(m[i])
        if tmp > n:
            n = tmp

    print("#{}".format(tc), end=' ')
    for i in range(n):
        for j in range(5):
            if i < len(m[j]):
                print(m[j][i], end='')
    print()