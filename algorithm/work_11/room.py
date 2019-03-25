def room(n):
    global N, cnt
    if n == N:
        return
    else:
        for i in range(cnt):
            flag = 0
            for j in range(len(r[i])):
                if m[n][r[i][j]]:
                    flag = 1
                    break
            if not flag:
                r[i].append(n)
                break
            elif flag and i == cnt - 1:
                r[cnt] = [n]
                cnt += 1
        print(r)
        room(n + 1)



for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    r = [0] * 4
    r[0] = [0]
    cnt = 1

    room(1)
    print(cnt)



"""
1
9
0 0 0 0 0 0 1 1 1
0 0 0 1 0 0 0 1 1
0 0 0 0 0 0 0 0 1
0 1 0 0 1 1 0 0 0
0 0 0 1 0 0 0 0 0
0 0 0 1 0 0 0 0 0
1 0 0 0 0 0 0 0 0
1 1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0

1
9
0 1 1 1 0 0 0 0 0
1 0 1 0 0 0 1 0 0
1 1 0 0 0 0 0 0 0
1 0 0 0 1 1 0 0 1
0 0 0 1 0 1 0 0 0
0 0 0 1 1 0 1 0 0
0 1 0 0 0 1 0 0 1
0 0 0 0 0 0 0 0 1
0 0 0 1 0 0 1 1 0
"""