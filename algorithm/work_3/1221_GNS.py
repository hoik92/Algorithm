import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    t, N = input().split()
    other = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    sample = input().split()
    cnt = [0] * 10

    for i in sample:
        for j in range(len(other)):
            if i == other[j]:
                cnt[j] += 1
                break

    print(t)
    for i in range(len(cnt)):
        print((other[i] + ' ') * cnt[i], end='')
    print()