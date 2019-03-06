def program(x, y):
    global result, top, memory, R, C, drt, cnt
    while True:
        visited.append((x, y))
        # if x == 0 and y == 1:
        #     if memory in stack:
        #         if cnt == 1000:
        #             result = "NO"
        #             # return
        #         else:
        #             cnt += 1
        #     else:
        #         stack[top] = memory
        #         top += 1
        if 48 <= ord(m[x][y]) <= 57:
            memory = int(m[x][y])
        elif m[x][y] == '<':
            drt = 2
        elif m[x][y] == '>':
            if (x, y) in visited and memory in stack and cnt == 5:
                result = "NO"
                return
            else:
                stack[top] = memory
                top += 1
                cnt += 1
            drt = 0
        elif m[x][y] == '^':
            drt = 3
        elif m[x][y] == 'v':
            drt = 1
        elif m[x][y] == '_':
            if memory:
                drt = 2
            else:
                drt = 0
        elif m[x][y] == '|':
            if memory:
                drt = 3
            else:
                drt = 1
        elif m[x][y] == '@':
            result = "YES"
            return
        elif m[x][y] == '-':
            memory -= 1
            if memory == -1:
                memory = 15
        elif m[x][y] == '+':
            memory += 1
            if memory == 16:
                memory = 0
        elif m[x][y] == '?':
            drt = (drt + 1) % 4
            print(result)
        x += dx[drt]
        y += dy[drt]
        if x == -1:
            x = R - 1
        elif x == R:
            x == 0
        if y == -1:
            y = C - 1
        elif y == C:
            y = 0

for tc in range(1, int(input())+1):
    R, C = map(int, input().split())
    m = [0] * R
    for i in range(R):
        m[i] = list(input())
    visited = []
    stack = [-1] * 15
    top = 0
    memory = 0
    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    drt = 0
    cnt = 0
    result = "YES"
    program(x, y)
    print(result)


# print(ord('0')) # 48
# print(ord('9')) # 57