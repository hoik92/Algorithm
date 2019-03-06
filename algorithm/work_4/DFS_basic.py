m = [0] * 7
for i in range(7):
    m[i] = [0] * 7

visited = [0] * 7
stack = [0] * 7
top = -1

inp = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = len(inp)
for i in range(N // 2):
    x, y = inp[2 * i], inp[2 * i + 1]
    m[x - 1][y - 1], m[y - 1][x - 1] = 1, 1

v = 1
print(v)
visited[v - 1] = 1
while True:
    for i in range(7):
        if m[v - 1][i] == 1 and visited[i] != 1:
            top += 1
            stack[top] = v
            w = i + 1
            break

    if top == -1:
        break

    while w:
        print(w)
        visited[w - 1] = 1
        top += 1
        stack[top] = w
        v = w
        for i in range(7):
            if m[v - 1][i] == 1 and visited[i] != 1:
                w = i + 1
                break
            else:
                w = 0
    v = stack[top]
    top -= 1
