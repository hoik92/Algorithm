import sys
sys.stdin = open('4836.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    
    base = [0]*10
    for i in range(10):
        base[i] = [0]*10
    
    red = []
    blue = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        if tmp[4] == 1:
            red.append(tmp)
        else:
            blue.append(tmp)

    for i in red:
        for c in range(i[0], i[2]+1):
            for r in range(i[1], i[3]+1):
                base[c][r] = 1
    
    cnt = 0
    for i in blue:
        for c in range(i[0], i[2]+1):
            for r in range(i[1], i[3]+1):
                if base[c][r] == 1:
                    base[c][r] = 3
                    cnt += 1
    
    print(f"#{tc} {cnt}")