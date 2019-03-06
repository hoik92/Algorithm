# import sys
# sys.stdin = open('input.txt', 'r')

A = [1,2,3,4,5,6,7,8,9,10,11,12]
n = len(A)

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    subset = []

    for i in range(1<<n):
        tmp = []
        for j in range(n):
            if i & (1<<j):
                tmp.append(A[j])
        if len(tmp) == N:
            subset.append(tmp)
    
    cnt = 0
    for i in range(len(subset)):
        subsum = 0
        for j in range(N):
            subsum += subset[i][j]
        if subsum == K:
            cnt += 1
    
    print(f"#{tc} {cnt}")