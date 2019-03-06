d = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]

r = []
for i in range(5):
    r.append([0]*5)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
rx, ry = 0, 0
drt = 0

for k in range(25):
    min_val = d[0][0]
    for i in range(5):
        for j in range(5):
            if min_val >= d[i][j]:
                min_val = d[i][j]
                x, y = i, j

    d[x][y] = 99

    if k == 0:
        r[0][0] = min_val
    else:
        if 0 <= rx + dx[drt] <= 4 and 0 <= ry + dy[drt] <= 4 and r[rx + dx[drt]][ry + dy[drt]] == 0:
            r[rx + dx[drt]][ry + dy[drt]] = min_val
            rx += dx[drt]
            ry += dy[drt]
        else:
            drt += 1
            drt = drt % 4
            r[rx + dx[drt]][ry + dy[drt]] = min_val
            rx += dx[drt]
            ry += dy[drt]

print(r)