def enQueue(item):
    global front, rear
    rear += 1
    queue[rear] = item

def deQueue():
    global front, rear
    front += 1
    item = queue[front]
    queue[front] = 0
    return item

def BFS():
    global result

    while front != rear:
        x, y = deQueue()
        if m[x][y] == '3':
            result = 1
            return
        for i in range(4):
            if m[x + dx[i]][y + dy[i]] != '1' and not visited[x + dx[i]][y + dy[i]]:
                visited[x + dx[i]][y + dy[i]] = 1
                enQueue((x + dx[i], y + dy[i]))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for t in range(10):
    tc = input()
    m = [0] * 100
    for i in range(100):
        m[i] = list(input())
    start_x, start_y = 1, 1
    visited = [[0] * 100 for _ in range(100)]
    queue = [0] * 10000
    front, rear = -1, -1

    visited[1][1] = 1
    enQueue((start_x, start_y))
    result = 0
    BFS()
    print("#{} {}".format(tc, result))