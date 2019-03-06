import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    happy = int(input())
    N -= 1
    r = []
    cnt = 0

    while N:
        happy = int(input())
        tmp = happy - 1
        if cnt == 0:
            cnt += 1
            r.append(tmp)
        else:
            idx = 0
            for i in range(cnt):
                if tmp % r[i] == 0:
                    break
                idx = i+1
            if idx == cnt:
                cnt += 1
                r.append(tmp)
        N -= 1
    print(f"#{tc} {cnt}")