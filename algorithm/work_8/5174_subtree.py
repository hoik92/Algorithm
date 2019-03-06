def preorder(t):
    global cnt
    if t:
        cnt += 1
        preorder(m[t][0])
        preorder(m[t][1])

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    m = [[0] * 2 for _ in range(E + 2)]
    M = list(map(int, input().split()))
    cnt = 0
    for i in range(E):
        if not m[M[2 * i]][0]:
            m[M[2 * i]][0] = M[2 * i + 1]
        else:
            m[M[2 * i]][1] = M[2 * i + 1]
    preorder(N)

    print("#{} {}".format(tc, cnt))