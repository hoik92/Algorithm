import sys
sys.stdin = open('input4881.txt', 'r')

def backtrack(a, k, N, tmp):
    global minsum

    if tmp > minsum:
        return
    if k == N-1:
        if minsum > tmp:
            minsum = tmp
    else:
        k += 1
        for i in range(N):
            if not a[i]:
                a[i] = 1
                tmp += m[k][i]
                backtrack(a, k, N, tmp)
                a[i] = 0
                tmp -= m[k][i]

for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    a = [0] * N
    k = -1
    minsum = 9 * N
    tmp = 0

    backtrack(a, k, N, tmp)
    print(f"#{tc} {minsum}")