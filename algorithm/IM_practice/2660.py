class Queue:
    def __init__(self, n):
        self.n = n
        self.queue = [0] * self.n
        self.rear, self.front = -1, -1

    def isEmpty(self):
        return self.rear == self.front

    def isFull(self):
        return self.rear == self.n - 1

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

def BFS():
    global N, queue, cnt
    while not queue.isEmpty():
        tmp, n = queue.deQueue()
        for i in range(1, N + 1):
            if m[n][i] and not visited[i]:
                queue.enQueue([tmp + 1, i])
                visited[i] = 1
                cnt = tmp + 1

N = int(input())
m = [[0] * (N + 1) for _ in range(N + 1)]
while True:
    x, y = map(int, input().split())
    if x == -1:
        break
    m[x][y], m[y][x] = 1, 1

score = [0] * (N + 1)
queue = Queue((N + 1) * (N + 1))
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    cnt = 0
    queue.enQueue([cnt, i])
    visited[i] = 1
    BFS()
    score[i] = cnt
# print(score)
min_score = N
candidate_cnt = 0
for i in range(1, N + 1):
    if min_score > score[i]:
        min_score = score[i]

for i in range(1, N + 1):
    if score[i] == min_score:
        candidate_cnt += 1

print(min_score, candidate_cnt)
for i in range(1, N + 1):
    if score[i] == min_score:
        print(i, end=' ')
print()