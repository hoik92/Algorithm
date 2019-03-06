import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    d = []

    for i in range((N//20) + int(bool(N%20))):
        tmp = input().split()
        for j in range(len(tmp)):
            d.append(tmp[j])
    
    for i in range(10**N):
        tmp = 0
        for j in range(N):
            if i // 10**j < 10:
                log = j
                break
        for j in range(log, log+1):
            for k in range(N - j):
                res = int(''.join(d[k:k+j+1]))
                if res == i:
                    tmp = 1
                    break
            if tmp == 1:
                break
        if tmp == 0:
            result = i
            break
    print(f"#{tc} {result}")