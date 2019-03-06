dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

class Queue:
    def __init__(self, N):
        self.N = N
        self.queue = [0] * (self.N ** 2)
        self.front, self.rear = -1, -1

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear == (self.N ** 2) - 1

    def enQueue(self, item):
        if not self.isFull():
            self.rear += 1
            self.queue[self.rear] = item

    def deQueue(self):
        if not self.isEmpty():
            self.front += 1
            item = self.queue[self.front]
            self.queue[self.front] = 0
            return item

def BFS(x, y):
    global q, N
    cnt = 0
    visited[x][y] = 1
    q.enQueue([x, y, cnt])
    while not q.isEmpty():
        item = q.deQueue()
        x, y, cnt = item[0], item[1], item[2]
        if m[x][y] == '3':
            return cnt - 1

        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and m[x+dx[i]][y+dy[i]] != '1' and not visited[x+dx[i]][y+dy[i]]:
                q.enQueue([x + dx[i], y + dy[i], cnt + 1])
                visited[x+dx[i]][y+dy[i]] = 1
    return 0

for tc in range(1, int(input())+1):
    N = int(input())
    m = [0] * N
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        m[i] = list(input())

    q = Queue(N)
    search = False
    for i in range(N):
        for j in range(N):
            if m[i][j] == '2':
                x, y = i, j
                search = True
                break
        if search:
            break

    result = BFS(x, y)
    print(f"#{tc} {result}")