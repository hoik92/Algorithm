# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    T = [[0]*N]
    cnt = 0
    for n in range(N):
        T.append(list(map(int, input().split())))
    T.append([0]*N)
    
    for x in range(N):
        for col in range(1, N+1):
            for row in range(N):
                if T[N+1-col][row] == 1:
                    if T[N+2-col][row] != 1 and T[N+2-col][row] != 2:
                        T[N+1-col][row] = 0
                        T[N+2-col][row] = 1
        for col in range(1, N+1):
            for row in range(N):
                if T[col][row] == 2:
                    if T[col-1][row] != 1 and T[col-1][row] != 2:
                        T[col][row] = 0
                        T[col-1][row] = 2
        T[0], T[N+1] = [0]*N, [0]*N

    for col in range(1, N+1):
        for row in range(N):
            if T[col][row] == 1 and T[col+1][row] == 2:
                cnt += 1
    print(f"#{tc} {cnt}")