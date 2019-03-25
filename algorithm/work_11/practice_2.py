# 조합 생성
def comb(n, r):
    if r == 0:
        print(t)
    elif n < r:
        return
    else:
        t[r - 1] = arr[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)


def comb2(k, s):
    global N, R
    if k == R:
        print(t)
    else:
        for i in range(s + 1, N):
            t[k] = arr[i]
            comb2(k + 1, i)


# 중복 조합 생성
def h_comb(k, s):
    global N, R
    if k == R:
        print(t)
    else:
        for i in range(s, N):
            t[k] = arr[i]
            h_comb(k + 1, i)


# 중복 순열 생성
def h_perm(k, r):
    global N
    if k == r:
        print(t)
    else:
        for i in range(N):
            t[k] = arr[i]
            h_perm(k + 1, r)


t = [0] * 2
arr = [1, 2, 3]
N, R = 3, 2  # N개 중에 R개 뽑겠다.
# comb(N, R)
# comb2(0, -1)
# h_comb(0, 0)
# h_perm(0, 2)
