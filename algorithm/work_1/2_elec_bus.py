# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    M_number = list(map(int, input().split()))

    cnt = 0
    tmp = 0

    for i in range(M):
        if tmp + K >= N:
            break
        for j in range(K):
            if tmp + K - j in M_number:
                tmp += K - j
                cnt += 1
                break

    for i in range(M - 1):
        if M_number[i + 1] - M_number[i] > K:
            cnt = 0
            break

    print(f"#{tc} {cnt}")
