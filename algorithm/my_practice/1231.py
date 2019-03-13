def inorder(n):
    if n:
        inorder(m[n][0])
        print(s[n], end='')
        inorder(m[n][1])

for tc in range(1, 11):
    N = int(input())
    m = [[0] * 2 for _ in range(N + 1)]
    s = [0] * (N + 1)

    for i in range(N):
        tmp = input().split()
        s[int(tmp[0])] = tmp[1]
        if len(tmp) >= 3:
            m[int(tmp[0])][0] = int(tmp[2])
            if len(tmp) == 4:
                m[int(tmp[0])][1] = int(tmp[3])

    print("#{}".format(tc), end=' ')
    inorder(1)
    print()