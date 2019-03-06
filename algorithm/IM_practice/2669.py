m = [[0] * 101 for _ in range(101)]
for _ in range(4):
    M = list(map(int, input().split()))
    for i in range(M[0], M[2]):
        for j in range(M[1], M[3]):
            m[i][j] = 1

cnt = 0
for i in range(1, 101):
    for j in range(1, 101):
        if m[i][j]:
            cnt += 1
print(cnt)