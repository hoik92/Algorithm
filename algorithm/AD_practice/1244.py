def change(N, cnt):
    global n, result
    if cnt == int(c):
        tmp = ""
        for i in N:
            tmp += i
        if int(tmp) > result:
            result = int(tmp)
        return
    else:
        M = [0] * n
        for i in range(n):
            M[i] = N[i]
        for i in range(n - 1):
            for j in range(i, n):
                M[i], M[j] = M[j], M[i]
                change(M, cnt + 1)

for tc in range(1, int(input())+1):
    N, c = input().split()
    N = list(N)
    n = len(N)
    cnt = 0
    result = 0
    change(N, cnt)
    print("#{} {}".format(tc, result))